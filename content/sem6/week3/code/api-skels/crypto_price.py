"""Crypto Price Tracker using CoinGecko API."""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv


class CryptoPriceTracker:
    """Tracks cryptocurrency prices using CoinGecko API."""
    
    BASE_URL = "https://api.coingecko.com/api/v3"
    
    def __init__(self):
        """Initialize the crypto tracker."""
        load_dotenv("../config/.env")
        self.api_key = os.getenv("COINGECKO_API_KEY")
    
    def get_price(self, coin_ids: List[str], vs_currencies: List[str] = ["inr"]) -> Dict:
        """Get current prices for specified cryptocurrencies."""
        url = f"{self.BASE_URL}/simple/price"
        params = {
            "ids": ",".join(coin_ids),
            "vs_currencies": ",".join(vs_currencies),
            "include_24hr_change": "true",
            "include_market_cap": "true"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_coin_details(self, coin_id: str) -> Dict:
        """Get detailed information about a specific cryptocurrency."""
        url = f"{self.BASE_URL}/coins/{coin_id}"
        params = {
            "localization": "false",
            "tickers": "false",
            "community_data": "false",
            "developer_data": "false"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_trending_coins(self) -> Dict:
        """Get trending cryptocurrencies."""
        url = f"{self.BASE_URL}/search/trending"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def track_portfolio(self, holdings: Dict[str, float]) -> Dict:
        """Track portfolio value for given holdings."""
        coin_ids = list(holdings.keys())
        prices = self.get_price(coin_ids, ["inr"])
        
        portfolio = {}
        total_value = 0
        
        for coin, amount in holdings.items():
            if coin in prices:
                price = prices[coin]["inr"]
                value = price * amount
                portfolio[coin] = {
                    "amount": amount,
                    "price_inr": price,
                    "value_inr": value,
                    "change_24h": prices[coin].get("inr_24h_change", 0)
                }
                total_value += value
        
        portfolio["total_value_inr"] = total_value
        return portfolio


def main():
    """Main execution function."""
    tracker = CryptoPriceTracker()
    
    coins = ["bitcoin", "ethereum", "cardano", "solana"]
    prices = tracker.get_price(coins, ["inr", "usd", "eur"])
    
    holdings = {"bitcoin": 0.5, "ethereum": 2.0, "cardano": 1000}
    portfolio = tracker.track_portfolio(holdings)
    
    trending = tracker.get_trending_coins()
    
    output_data = {
        "current_prices": prices,
        "portfolio_tracking": portfolio,
        "trending_coins": trending
    }
    
    output_path = Path("../output/crypto_price.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()
