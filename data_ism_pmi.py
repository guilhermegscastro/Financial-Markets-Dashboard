from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from datetime import timedelta
from datetime import datetime

def webscraping_ism_pmi():

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    # URL for ISM Manufacturing PMI data
    url = "https://www.investing.com/economic-calendar/ism-manufacturing-pmi-173"

    # Load the page
    driver.get(url)

    # Wait for the historical data section to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "historyTab"))
        )
    except Exception as e:
        print("Error loading the page:", e)
        driver.quit()
        exit()
    
    try:
        while True:
            show_more_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "showMoreReplies"))
            )
            show_more_button.click()
            time.sleep(1)  # Allow time for new data to load
    except:
        print("All data loaded or no more 'Show More' button available.")

    # Extract data from the table
    data = []

    rows = driver.find_elements(By.CSS_SELECTOR, 'tr[event_attr_id="173"]')

    for row in rows[1:]:  # Skip header row
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 5:
            release_date = cells[0].text.strip()
            actual = cells[2].text.strip()
            forecast = cells[3].text.strip()
            previous = cells[4].text.strip()
            data.append({
                "Release Date": release_date,
                "Actual": actual,
                "Forecast": forecast,
                "Previous": previous
            })

    # Close the browser
    driver.quit()

    # Save data to a DataFrame
    df = pd.DataFrame(data)

    df["Release Date"] = pd.to_datetime(df["Release Date"].str.extract(r"([A-Za-z]{3} \d{2}, \d{4})")[0], format="%b %d, %Y")

    today = datetime.now()
    start_date = today - timedelta(days = 4000)
    start_date = start_date.strftime('%Y-%m-%d')

    df = df[df["Release Date"] >= pd.to_datetime(start_date)]

    df.to_csv("ism_manufacturing_pmi.csv", index=False)

    print("Scraping completed. Data saved to ism_manufacturing_pmi.csv")

if __name__ == "__main__":

    webscraping_ism_pmi()
    