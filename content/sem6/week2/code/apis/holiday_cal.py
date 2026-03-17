"""Public Holiday Calendar API integrating Nager Date API."""

import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class HolidayCalendar:
    """Fetches public holidays using Nager Date API."""
    
    BASE_URL = "https://date.nager.at/api/v3"
    
    def get_holidays(self, year: int, country_code: str) -> List[Dict]:
        """Get all public holidays for a specific year and country."""
        try:
            url = f"{self.BASE_URL}/PublicHolidays/{year}/{country_code}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return [{"error": str(e), "country": country_code}]
    
    def get_next_holidays(self, country_code: str) -> List[Dict]:
        """Get upcoming public holidays for a country."""
        try:
            url = f"{self.BASE_URL}/NextPublicHolidays/{country_code}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return [{"error": str(e), "country": country_code}]
    
    def is_public_holiday(self, date: str, country_code: str) -> Dict:
        """Check if a specific date is a public holiday."""
        try:
            url = f"{self.BASE_URL}/IsTodayPublicHoliday/{country_code}"
            response = requests.get(url, timeout=10)
            return {
                "date": date,
                "country_code": country_code,
                "is_holiday": response.status_code == 200
            }
        except Exception as e:
            return {
                "date": date,
                "country_code": country_code,
                "error": str(e)
            }
    
    def get_available_countries(self) -> List[Dict]:
        """Get list of available countries."""
        try:
            url = f"{self.BASE_URL}/AvailableCountries"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return [{"error": str(e)}]
    
    def get_holidays_safe(self, year: int, country_code: str) -> Dict:
        """Get holidays with comprehensive error handling and status."""
        result = {
            "country_code": country_code,
            "year": year,
            "success": False,
            "holidays": [],
            "error": None
        }
        
        try:
            url = f"{self.BASE_URL}/PublicHolidays/{year}/{country_code}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            result["holidays"] = response.json()
            result["success"] = True
            result["count"] = len(result["holidays"])
        except requests.exceptions.ConnectionError:
            result["error"] = "Network connection failed. Please check internet connectivity."
        except requests.exceptions.Timeout:
            result["error"] = "Request timed out. API may be slow or unavailable."
        except requests.exceptions.HTTPError as e:
            result["error"] = f"HTTP error: {e.response.status_code}"
        except Exception as e:
            result["error"] = f"Unexpected error: {str(e)}"
        
        return result


def main():
    """Main execution function."""
    calendar = HolidayCalendar()
    
    current_year = datetime.now().year
    countries = ["IN"]
    
    holidays_by_country = {}
    for country in countries:
        holidays_by_country[country] = calendar.get_holidays_safe(current_year, country)
    
    next_holidays_result = {
        "country": "IN",
        "success": False,
        "holidays": []
    }
    
    try:
        next_holidays = calendar.get_next_holidays("IN")
        if next_holidays and not any("error" in h for h in next_holidays):
            next_holidays_result["success"] = True
            next_holidays_result["holidays"] = next_holidays
        else:
            next_holidays_result["error"] = "Failed to fetch next holidays"
    except Exception as e:
        next_holidays_result["error"] = str(e)
    
    output_data = {
        "year": current_year,
        "country": "IN",
        "holidays_by_country": holidays_by_country,
        "next_indian_holidays": next_holidays_result,
        "api_status": "Check individual country results for errors"
    }
    
    output_path = Path("..output/holiday_cal.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)
    
    print(f"Indian holiday data saved to {output_path}")
    
    if not holidays_by_country.get("IN", {}).get("success", False):
        print("Warning: Failed to fetch Indian holidays")


if __name__ == "__main__":
    main()
