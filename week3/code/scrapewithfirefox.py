
import os
import pandas as pd
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By

OUTPUT_DIR = "../output/"

class WebScraper:
    def __init__(self, url: str, output_directory: str):
        self.target_url = url
        self.output_dir = output_directory
        self.file_path = self._generate_file_path()
        self.driver = None

    def _generate_file_path(self) -> str:
        parsed_url = urlparse(self.target_url)
        path_part = parsed_url.path.replace('/', '_').strip('_')
        file_name = f"{path_part}.csv"
        os.makedirs(self.output_dir, exist_ok=True)
        return os.path.join(self.output_dir, file_name)

    def _scrape_with_pandas(self) -> bool:
        print("Attempting to scrape table directly with pandas.read_html()...")
        try:
            tables = pd.read_html(self.target_url)
            if tables:
                df = tables[0]
                self._save_to_csv(df)
                return True
            else:
                print("No tables found by pandas.read_html().")
                return False
        except Exception as e:
            print(f"Could not use pandas.read_html(): {e}. Falling back to Selenium.")
            return False

    def _initialize_driver(self) -> None:
        if self.driver is None:
            print("Initializing Firefox WebDriver...")
            self.driver = webdriver.Firefox()
            print("WebDriver initialized.")

    def _scrape_with_selenium(self) -> pd.DataFrame:
        self._initialize_driver()
        print(f"Navigating to {self.target_url}...")
        self.driver.get(self.target_url)
        
        print("Scraping data from the table...")
        table_element = self.driver.find_element(By.CLASS_NAME, "wikitable")
        
        df = pd.read_html(table_element.get_attribute('outerHTML'))[0]
        
        print(f"Successfully scraped table with {len(df)} rows using Selenium.")
        return df

    def _save_to_csv(self, dataframe: pd.DataFrame):
        if not dataframe.empty:
            print(f"Saving data to '{self.file_path}'...")
            dataframe.to_csv(self.file_path, index=False)
            print("Successfully saved data.")
        else:
            print("No data found to save.")

    def _close_browser(self):
        if self.driver:
            print("Closing the browser.")
            self.driver.quit()

    def run(self):
        try:
            if not self._scrape_with_pandas():
                scraped_df = self._scrape_with_selenium()
                self._save_to_csv(scraped_df)
        finally:
            self._close_browser()

def main():
    default_url = "https://en.wikipedia.org/wiki/Java_version_history"
    
    try:
        user_input = input(f"Enter URL to scrape (or press Enter for default: {default_url}): ")
        target_url = user_input.strip() if user_input.strip() else default_url
        
        scraper = WebScraper(url=target_url, output_directory=OUTPUT_DIR)
        scraper.run()
        
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()



