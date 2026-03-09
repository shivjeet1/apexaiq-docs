"""News Aggregation API service fetching top headlines from NewsAPI."""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv


class NewsAggregator:
    """Fetches top headlines from NewsAPI."""
    
    BASE_URL = "https://newsapi.org/v2/top-headlines"
    
    def __init__(self):
        """Initialize the news aggregator with API key."""
        load_dotenv("../config/.env")
        self.api_key = os.getenv("NEWSAPI_KEY")
    
    def get_top_headlines(self, country: str = "us", category: Optional[str] = None, # ISO 3166-1 alpha-2 country code
                         page_size: int = 20) -> Dict:
        """Fetch top headlines by country and category."""
        params = {
            "apiKey": self.api_key,
            "country": country,
            "pageSize": page_size
        }
        
        if category:
            params["category"] = category
        
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_headlines_by_source(self, sources: List[str], page_size: int = 20) -> Dict:
        """Fetch headlines from specific news sources."""
        params = {
            "apiKey": self.api_key,
            "sources": ",".join(sources),
            "pageSize": page_size
        }
        
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    
    def aggregate_news(self, categories: List[str], country: str = "us") -> Dict[str, List]:
        """Aggregate news across multiple categories."""
        aggregated = {}
        
        for category in categories:
            data = self.get_top_headlines(country=country, category=category, page_size=10)
            aggregated[category] = data.get("articles", [])
        
        return aggregated


def main():
    """Main execution function."""
    aggregator = NewsAggregator()
    
    categories = ["technology", "business", "science"]
    news_data = aggregator.aggregate_news(categories)
    
    output_data = {
        "country": "us",
        "categories": categories,
        "news_by_category": news_data,
        "total_articles": sum(len(articles) for articles in news_data.values())
    }
    
    output_path = Path("../output/top_headlines.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()

