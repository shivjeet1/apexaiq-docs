
import os
import re
import pandas as pd
from datetime import datetime
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

OUTPUT_DIR = "../../output/"

class DbfNewsScraper:
    def __init__(self, url: str, output_directory: str):
        self.target_url = url
        self.output_dir = output_directory
        self.file_path = self._generate_file_path()
        self.driver = None

    def _generate_file_path(self) -> str:
        file_name = "custom-scrapped-data.csv"
        os.makedirs(self.output_dir, exist_ok=True)
        return os.path.join(self.output_dir, file_name)

    def _initialize_driver(self) -> None:
        if self.driver is None:
            print("Initializing Firefox WebDriver...")
            self.driver = webdriver.Firefox()
            print("WebDriver initialized.")

    def _scrape_and_process_data(self) -> pd.DataFrame | None:
        self._initialize_driver()
        print(f"Navigating to {self.target_url}...")
        self.driver.get(self.target_url)

        print("Waiting for news content (<h3> tags) to load...")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
            )
        except TimeoutException:
            print("Timeout: No <h3> elements found after 10 seconds. Cannot scrape data.")
            return None

        print("Scraping and processing release information...")
        heading_elements = self.driver.find_elements(By.TAG_NAME, "h3")
        
        release_data = []

        for i, heading in enumerate(heading_elements):
            try:
                heading_text = heading.text
                
                match = re.search(r'VERSION\s+(v[\d.]+)\s+\((.*)\)', heading_text)
                if not match:
                    print(f"  - Skipping heading: Text '{heading_text}' does not match expected format.")
                    continue

                version = match.group(1)
                date_str = match.group(2)

                link_element = heading.find_element(By.XPATH, "following-sibling::p[1]//a")
                relative_url = link_element.get_attribute('href')
                dl_url = urljoin(self.target_url, relative_url)

                try:
                    parsed_date = datetime.strptime(date_str.strip(), '%B %d, %Y')
                    formatted_date = parsed_date.strftime('%Y-%m-%d')
                except ValueError:
                    print(f"  - Could not parse date '{date_str}'. Keeping original format.")
                    formatted_date = date_str

                release_data.append({
                    "Version": version,
                    "Date": formatted_date,
                    "URL": dl_url,
                })
                print(f"  - Scraped: Version={version}, Date={formatted_date}")

            except NoSuchElementException:
                print(f"  - Warning: Could not find a download link for heading: '{heading.text}'")
            except Exception as e:
                print(f"  - An error occurred while processing an entry: {e}")

        if not release_data:
            print("No valid release data was scraped from the page.")
            return None

        return pd.DataFrame(release_data)

    def _save_data_to_csv(self, dataframe: pd.DataFrame | None):
        if dataframe is None or dataframe.empty:
            print("No data to save.")
            return

        print(f"Saving scraped data to '{self.file_path}'...")
        dataframe.to_csv(self.file_path, index=False)
        print(f"Successfully saved {len(dataframe)} records to {self.file_path}")

    def _close_browser(self):
        if self.driver:
            print("Closing the browser.")
            self.driver.quit()
    
    def run(self):
        scraped_df = None
        try:
            scraped_df = self._scrape_and_process_data()
            self._save_data_to_csv(scraped_df)
        finally:
            self._close_browser()

def main():
    try:
        target_url = ""
        while not target_url:
            user_input = input("Please enter the full URL to scrape: ")
            target_url = user_input.strip()
            if not target_url:
                print("URL cannot be empty. Please try again.")

        print(f"Starting scraper for: {target_url}")
        scraper = DbfNewsScraper(url=target_url, output_directory=OUTPUT_DIR)
        scraper.run()
        
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred in the main process: {e}")

if __name__ == "__main__":
    main()


