from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Setup
service = Service("D:/Software Tester/selenium_test/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Search something
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait and close
time.sleep(5)
driver.quit()
