"""Weather Dashboard API service for fetching and caching OpenWeatherMap data."""

import os
import json
import time
import requests
from pathlib import Path
from typing import Dict, Optional
from dotenv import load_dotenv


class WeatherDashboard:
    """Fetches and caches weather data from OpenWeatherMap API."""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    CACHE_DURATION = 600  # seconds
    
    def __init__(self):
        """Initialize the weather dashboard with API key."""
        load_dotenv("../config/.env")
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.cache: Dict[str, Dict] = {}
        
    def _is_cache_valid(self, city: str) -> bool:
        """Check if cached data is still valid."""
        if city not in self.cache:
            return False
        return time.time() - self.cache[city]["timestamp"] < self.CACHE_DURATION
    
    def get_weather(self, city: str) -> Dict:
        """Fetch weather data for a city with caching."""
        if self._is_cache_valid(city):
            return self.cache[city]["data"]
        
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        self.cache[city] = {"data": data, "timestamp": time.time()}
        return data
    
    def get_multiple_cities(self, cities: list) -> Dict[str, Dict]:
        """Fetch weather data for multiple cities."""
        results = {}
        for city in cities:
            try:
                results[city] = self.get_weather(city)
            except Exception as e:
                results[city] = {"error": str(e)}
        return results


def main():
    """Main execution function."""
    dashboard = WeatherDashboard()
    
    cities = ["Mumbai", "Amravati", "Akola", "Shegaon"]
    weather_data = dashboard.get_multiple_cities(cities)
    
    output_path = Path("../output/weather_data.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(weather_data, f, indent=2)


if __name__ == "__main__":
    main()
