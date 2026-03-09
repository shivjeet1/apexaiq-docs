"""Quote of the Day API integrating ZenQuotes API with caching."""

import json
import time
import requests
from pathlib import Path
from typing import Dict, List, Optional


class QuoteOfTheDay:
    """Fetches quotes from ZenQuotes API with caching."""
    
    BASE_URL = "https://zenquotes.io/api"
    CACHE_DURATION = 86400  # 24 hours
    
    def __init__(self):
        """Initialize the quote service."""
        self.cache: Dict[str, Dict] = {}
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid."""
        if cache_key not in self.cache:
            return False
        return time.time() - self.cache[cache_key]["timestamp"] < self.CACHE_DURATION
    
    def get_today_quote(self) -> Dict:
        """Get quote of the day with caching."""
        cache_key = "today"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]["data"]
        
        url = f"{self.BASE_URL}/today"
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()[0]
        self.cache[cache_key] = {"data": data, "timestamp": time.time()}
        return data
    
    def get_random_quotes(self, count: int = 5) -> List[Dict]:
        """Get random quotes."""
        url = f"{self.BASE_URL}/quotes"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[:count]
    
    def get_quotes_by_keyword(self, keyword: str) -> List[Dict]:
        """Get quotes containing a specific keyword."""
        quotes = self.get_random_quotes(50)
        return [q for q in quotes if keyword.lower() in q.get("q", "").lower()]


def main():
    """Main execution function."""
    quote_service = QuoteOfTheDay()
    
    today_quote = quote_service.get_today_quote()
    random_quotes = quote_service.get_random_quotes(10)
    
    output_data = {
        "quote_of_the_day": today_quote,
        "random_quotes": random_quotes,
        "total_random": len(random_quotes)
    }
    
    output_path = Path("../output/quote_daily.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()
