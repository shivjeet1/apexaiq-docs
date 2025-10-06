#!/bin/sh

import requests
import string
import os
import random

class WallhavenClient:
    BASE_URL = "https://wallhaven.cc/api/v1/search"

    def search_wallpapers(self, query_obj):
        params = {'q': query_obj.get_text()}
        try:
            res = requests.get(self.BASE_URL, params=params, timeout=15)
            res.raise_for_status()
            json_data = res.json()
            return [item["path"] for item in json_data.get("data", [])]
        except requests.exceptions.RequestException as e:
            print(f"Error: An API or network error occurred: {e}")
            return []

class WallpaperDownloader:
    def __init__(self, download_directory):
        self._download_dir = download_directory
        self._ensure_dir_exists()

    def _ensure_dir_exists(self):
        os.makedirs(self._download_dir, exist_ok=True)

    def _generate_random_id(self, length=6):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=length))

    def download(self, url):
        try:
            print(f"Downloading: {url}")
            res = requests.get(url, timeout=30)
            res.raise_for_status()

            wallpaper_name = self._generate_random_id()
            extension = os.path.splitext(url)[1] or '.jpg'
            download_path = os.path.join(self._download_dir, f"{wallpaper_name}{extension}")
            
            with open(download_path, 'wb') as f:
                f.write(res.content)
            print(f"Saved to: {download_path}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to download {url}. Reason: {e}")
            return False

class SearchQuery:
    def __init__(self, text):
        self._text = text.strip()

    def get_text(self):
        return self._text

def main():
    DOWNLOAD_PATH = "wallpapers"
    print("--- Wallhaven Wallpaper Downloader ---")
    
    client = WallhavenClient()
    downloader = WallpaperDownloader(DOWNLOAD_PATH)

    raw_input = input('Enter a theme to search for: ')
    if not raw_input:
        print("Search cannot be empty. Exiting.")
        return

    query = SearchQuery(raw_input)
    wallpaper_urls = client.search_wallpapers(query)

    if not wallpaper_urls:
        print(f"No wallpapers found for the theme: '{query.get_text()}'")
        return

    print(f"Found {len(wallpaper_urls)} wallpapers. Starting download process...")
    download_count = 0
    for url in wallpaper_urls:
        if downloader.download(url):
            download_count += 1
    
    print(f"\nDownload complete. Successfully downloaded {download_count} wallpapers to the '{DOWNLOAD_PATH}' folder.")

if __name__ == "__main__":
    main()

