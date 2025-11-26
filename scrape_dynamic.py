import time
from pathlib import Path
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

WAIT = 40

class DynamicScraper:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, WAIT)
        self.dataframes = []

    def run(self):
        url = "https://voters.eci.gov.in/download-eroll?stateCode=S04"
        self.driver.get(url)

        try:
            district_select = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//select[@aria-label='District']"))
            )
        except TimeoutException:
            print("District dropdown not found.")
            return

        selectable = Select(district_select)

        for opt in selectable.options[1:]:
            value = opt.get_attribute("value")
            if not value:
                continue

            selectable.select_by_value(value)
            time.sleep(2)

            try:
                show_btn = self.wait.until(
                    EC.element_to_be_clickable((By.ID, "btnshow"))
                )
                show_btn.click()
            except:
                continue

            try:
                table = self.wait.until(
                    EC.presence_of_element_located((By.ID, "cardTable"))
                )
            except TimeoutException:
                print(f"Timeout for District: {opt.text}")
                continue

            html = table.get_attribute("outerHTML")
            df = pd.read_html(html)[0]
            self.dataframes.append(df)
            print(f"Fetched table for {opt.text}")

        outdir = Path("selenium_dynamic_scraper/selenium_output")
        outdir.mkdir(exist_ok=True)
        combined = pd.concat(self.dataframes, ignore_index=True)
        combined.to_csv(outdir / "combined.csv", index=False)
        print("Saved combined.csv")

        self.driver.quit()

if __name__ == "__main__":
    scraper = DynamicScraper(headless=True)
    scraper.run()

