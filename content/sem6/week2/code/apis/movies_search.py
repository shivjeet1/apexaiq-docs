"""Movie Search API service integrating OMDb API with pagination and filtering."""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv


class MovieSearchAPI:
    """Searches movies using OMDb API with pagination and filtering."""
    
    BASE_URL = "http://www.omdbapi.com/"
    
    def __init__(self):
        """Initialize the movie search API with API key."""
        load_dotenv("../config/.env")
        self.api_key = os.getenv("OMDB_API_KEY")
    
    def search(self, query: str, page: int = 1, year: Optional[str] = None, 
               movie_type: Optional[str] = None) -> Dict:
        """Search for movies with pagination and filtering."""
        params = {
            "apikey": self.api_key,
            "s": query,
            "page": page
        }
        
        if year:
            params["y"] = year
        if movie_type:
            params["type"] = movie_type
        
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_details(self, imdb_id: str) -> Dict:
        """Get detailed information about a specific movie."""
        params = {"apikey": self.api_key, "i": imdb_id, "plot": "full"}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    
    def search_with_filters(self, query: str, pages: int = 2, 
                           year: Optional[str] = None) -> List[Dict]:
        """Search across multiple pages and return combined results."""
        all_results = []
        
        for page in range(1, pages + 1):
            data = self.search(query, page=page, year=year)
            if data.get("Response") == "True":
                all_results.extend(data.get("Search", []))
        
        return all_results


def main():
    """Main execution function."""
    api = MovieSearchAPI()
    
    search_results = api.search_with_filters("The Kashmir Files", pages=1)
    
    detailed_results = []
    for movie in search_results[:5]:
        details = api.get_details(movie["imdbID"])
        detailed_results.append(details)
    
    output_data = {
        "search_query": "The Kashmir Files",
        "total_results": len(search_results),
        "detailed_movies": detailed_results
    }
    
    output_path = Path("../output/movies_search.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()
