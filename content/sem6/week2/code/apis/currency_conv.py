"""Currency Conversion Service using ExchangeRate-API."""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List
from dotenv import load_dotenv


class CurrencyConverter:
    """Converts currencies using ExchangeRate-API."""
    
    BASE_URL = "https://v6.exchangerate-api.com/v6"
    
    def __init__(self):
        """Initialize the currency converter with API key."""
        load_dotenv("../config/.env")
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    
    def get_exchange_rates(self, base_currency: str) -> Dict:
        """Get all exchange rates for a base currency."""
        url = f"{self.BASE_URL}/{self.api_key}/latest/{base_currency}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> Dict:
        """Convert amount from one currency to another."""
        url = f"{self.BASE_URL}/{self.api_key}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def bulk_convert(self, amount: float, from_currency: str, 
                    to_currencies: List[str]) -> Dict[str, float]:
        """Convert amount to multiple currencies."""
        rates_data = self.get_exchange_rates(from_currency)
        rates = rates_data.get("conversion_rates", {})
        
        conversions = {}
        for currency in to_currencies:
            if currency in rates:
                conversions[currency] = round(amount * rates[currency], 2)
        
        return conversions


def main():
    """Main execution function."""
    converter = CurrencyConverter()
    
    amount = 100
    base = "INR"
    targets = ["EUR", "GBP", "JPY", "USD", "AUD"]
    
    conversions = converter.bulk_convert(amount, base, targets)
    single_conversion = converter.convert(amount, base, "EUR")
    
    output_data = {
        "base_amount": amount,
        "base_currency": base,
        "bulk_conversions": conversions,
        "detailed_conversion_example": single_conversion
    }
    
    output_path = Path("../output/currency_conv.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()
