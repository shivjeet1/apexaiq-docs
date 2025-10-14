
import os
import pandas as pd
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def _scrape_with_pandas(self) -> list[pd.DataFrame] | None:
        print("Attempting to scrape all tables directly with pandas.read_html()...")
        try:
            tables = pd.read_html(self.target_url)
            if tables:
                print(f"Pandas found {len(tables)} table(s).")
                return tables
            else:
                print("No tables found by pandas.read_html().")
                return None
        except Exception as e:
            print(f"Could not use pandas.read_html(): {e}. Falling back to Selenium.")
            return None

    def _initialize_driver(self) -> None:
        if self.driver is None:
            print("Initializing Firefox WebDriver...")
            self.driver = webdriver.Firefox()
            print("WebDriver initialized.")

    def _scrape_with_selenium(self) -> list[pd.DataFrame]:
        self._initialize_driver()
        print(f"Navigating to {self.target_url}...")
        self.driver.get(self.target_url)
        
        print("Waiting for tables with XPath matching the 'wikitable' class to load...")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'wikitable')]"))
            )
        except TimeoutException:
            print("Timeout: No elements matching the XPath found after 10 seconds.")
            return []

        print("Scraping data from all found tables...")
        table_elements = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'wikitable')]")
        
        dfr = []
        for i, table_element in enumerate(table_elements):
            html = table_element.get_attribute('outerHTML')
            df = pd.read_html(html)[0]
            dfr.append(df)
            print(f"  - Scraped table {i+1} with {len(df)} rows.")
            
        return dfr

    def _save_concatenated_csv(self, dataframes: list[pd.DataFrame] | None):
        if not dataframes:
            print("No dataframes found to save.")
            return

        print(f"Found {len(dataframes)} dataframe(s). Preparing to combine into one CSV.")
        
        all_tables_to_combine = []
        
        for i, df in enumerate(dataframes):
            if i >= 0:
                all_tables_to_combine.append(pd.DataFrame([[]]))
                heading = f"--- Table {i + 1} ---"
                all_tables_to_combine.append(pd.DataFrame([heading]))

            all_tables_to_combine.append(df)

        final_df = pd.concat(all_tables_to_combine, ignore_index=True)
        
        file_path = f"{self.file_path}_all_tables.csv"
        print(f"Saving combined data to '{file_path}'...")
        
        final_df.to_csv(file_path, index=False, header=False)
        print("Successfully saved combined data.")

    def _close_browser(self):
        if self.driver:
            print("Closing the browser.")
            self.driver.quit()

    def run(self):
        scraped_dfs = None
        try:
            scraped_dfs = self._scrape_with_pandas()
            if scraped_dfs is None:
                scraped_dfs = self._scrape_with_selenium()
            
            self._save_concatenated_csv(scraped_dfs)
        finally:
            self._close_browser()

def main():
    try:
        target_url = "https://en.wikipedia.org/wiki/SUSE_Linux_Enterprise"
        while not target_url:
            user_input = input(f"Enter full URL to scrape : ): ")
            target_url = user_input.strip()
            if not target_url:
                print("URL cannot be empty. Please try again.")
        print(f"Starting scraper for: {target_url}")
        scraper = WebScraper(url=target_url, output_directory=OUTPUT_DIR)
        scraper.run()
        
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

