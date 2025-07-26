import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setup folder to save HTML files
folder_path = r"D:\Software Tester\Laptop_data"
os.makedirs(folder_path, exist_ok=True)

driver_path = "D:\\Software Tester\\selenium_test\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    # Open Amazon and search for laptops
    driver.get("https://www.amazon.in")
    time.sleep(3)

    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for search results to load

    page_number = 1

    while True:
        # Wait for product titles or main results container
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
        except TimeoutException:
            print("Search results did not load properly, exiting.")
            break

        # Save current page HTML to file
        html_content = driver.page_source
        file_path = os.path.join(folder_path, f"amazon_laptop_page_{page_number}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Saved HTML of page {page_number}")

        # Try to go to the next page
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
            # Check if next button is disabled
            if "s-pagination-disabled" in next_button.get_attribute("class"):
                print("No more pages found. Exiting.")
                break
            else:
                next_button.click()
                page_number += 1
                time.sleep(5)  # wait for the next page to load
        except NoSuchElementException:
            print("Next button not found. Exiting.")
            break

finally:
    driver.quit()
