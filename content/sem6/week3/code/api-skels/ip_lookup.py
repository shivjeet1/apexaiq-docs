"""Geolocation Lookup API using ip-api to fetch location details from IP."""

import json
import requests
from pathlib import Path
from typing import Dict, List


class GeolocationLookup:
    """Fetches geolocation data from IP addresses using ip-api."""
    
    BASE_URL = "http://ip-api.com/json"
    
    def get_location(self, ip_address: str = "") -> Dict:
        """Get geolocation details for an IP address."""
        url = f"{self.BASE_URL}/{ip_address}" if ip_address else self.BASE_URL
        params = {
            "fields": "status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def batch_lookup(self, ip_addresses: List[str]) -> List[Dict]:
        """Perform batch geolocation lookup for multiple IPs."""
        url = "http://ip-api.com/batch"
        params = {
            "fields": "status,message,country,countryCode,region,regionName,city,lat,lon,timezone,isp,query"
        }
        
        response = requests.post(url, json=ip_addresses, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_current_location(self) -> Dict:
        """Get geolocation for the current IP."""
        return self.get_location()


def main():
    """Main execution function."""
    geo = GeolocationLookup()
    
    current_location = geo.get_current_location()
    
    test_ips = ["8.8.8.8", "1.1.1.1", "208.67.222.222"]
    batch_results = geo.batch_lookup(test_ips)
    
    output_data = {
        "current_ip_location": current_location,
        "batch_lookup_results": batch_results,
        "total_lookups": len(batch_results)
    }
    
    output_path = Path("../output/ip_lookup.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()
