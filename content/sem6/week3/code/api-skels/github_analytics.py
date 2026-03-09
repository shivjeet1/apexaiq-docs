"""GitHub Analytics Service fetching repository stats from GitHub REST API."""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv


class GitHubAnalytics:
    """Fetches repository statistics from GitHub REST API."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self):
        """Initialize the GitHub analytics service with token."""
        load_dotenv("../config/.env")
        self.token = os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_repo_stats(self, owner: str, repo: str) -> Dict:
        """Get detailed statistics for a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        data = response.json()
        return {
            "name": data["name"],
            "full_name": data["full_name"],
            "description": data["description"],
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "language": data["language"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"]
        }
    
    def get_contributors(self, owner: str, repo: str) -> List[Dict]:
        """Get top contributors for a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/contributors"
        params = {"per_page": 10}
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        
        return [{
            "login": c["login"],
            "contributions": c["contributions"],
            "avatar_url": c["avatar_url"]
        } for c in response.json()]
    
    def get_languages(self, owner: str, repo: str) -> Dict[str, int]:
        """Get programming languages used in a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/languages"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_recent_commits(self, owner: str, repo: str, count: int = 10) -> List[Dict]:
        """Get recent commits for a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits"
        params = {"per_page": count}
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        
        return [{
            "sha": c["sha"][:7],
            "author": c["commit"]["author"]["name"],
            "message": c["commit"]["message"],
            "date": c["commit"]["author"]["date"]
        } for c in response.json()]
    
    def analyze_repository(self, owner: str, repo: str) -> Dict:
        """Perform comprehensive analysis of a repository."""
        return {
            "stats": self.get_repo_stats(owner, repo),
            "contributors": self.get_contributors(owner, repo),
            "languages": self.get_languages(owner, repo),
            "recent_commits": self.get_recent_commits(owner, repo, 5)
        }


def main():
    """Main execution function."""
    analytics = GitHubAnalytics()
    
    repos = [
        ("shivjeet1", "apexaiq-docs"),
        ("torvalds", "linux"),
        ("python", "cpython")
    ]
    
    analysis_results = {}
    for owner, repo in repos:
        try:
            analysis_results[f"{owner}/{repo}"] = analytics.analyze_repository(owner, repo)
        except Exception as e:
            analysis_results[f"{owner}/{repo}"] = {"error": str(e)}
    
    output_data = {
        "analyzed_repositories": repos,
        "analysis": analysis_results
    }
    
    output_path = Path("../output/github_analytics.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()
