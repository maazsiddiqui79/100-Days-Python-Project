from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from collecting_data import Rental_Web_Scraper


URL = 'https://appbrewery.github.io/Zillow-Clone/'

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)
driver.get(url=URL)

elements = driver.find_elements(by=By.CLASS_NAME, value="StyledCard-c11n-8-84")
print(elements)

file = 0
for i in elements:
    data = i.get_attribute("outerHTML")
    with open(f"database/Rental_Rooms_{file}.html", "w", encoding="utf-8") as f:
        f.write(data)
        file += 1

    print(i)
    print(i.tag_name)
    print(i.text)
    print("+-------------------------------+")

rent = Rental_Web_Scraper(folder_path='database')
