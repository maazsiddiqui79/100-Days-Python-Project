from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Collecting_Data 

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

query = input("Please enter the name of the product you want to search on Amazon: ".title())
file = 0

for p in range(15):
    driver = webdriver.Chrome(options=chrome)
    driver.get(url=f"https://www.amazon.in/s?k={query}&page={p}&crid=15DEBI9LO0CQM&sprefix=laptop%2Caps%2C207&ref=nb_sb_noss_2")

    elem = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    
    for i in elem:
        d = i.get_attribute("outerHTML")
        with open(fr"data-base\{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            
            file+=1
            
            
    driver.close()
    
amazon = Collecting_Data.AmazonScraper(folder_path="data-base",filename="Exported_Data.csv")
