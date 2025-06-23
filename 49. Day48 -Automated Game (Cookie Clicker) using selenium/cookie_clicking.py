#----------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep ,time
import random

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
# Don't use 'detach' here — it's not supported in this context

# Start undetected Chrome
driver = uc.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Set language to English
sleep(3)
driver.execute_script('localStorage.setItem("CookieClickerLang", "EN");')
driver.refresh()

# Wait for the big cookie to load
try:
    cookie = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
    print("Game loaded. Ready to click the cookie.")
except Exception as e:
    print("Game did not load properly:", e)
    

# cookie = driver.find_element(by=By.ID,value="bigCookie")

item_ids = [f"product{i}" for i in range(18)]

wait_time = 5 
stop_time = time() + wait_time

while True:
    cookie.click()
    
    
    if time() >stop_time:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",",""))
            products = driver.find_elements(By.CSS_SELECTOR,"div[id^='product']")
            
            upgrade = driver.find_elements(By.CSS_SELECTOR,"div[id^='upgrade']")
                        
            best = None
            best2 = None
            for i in reversed(upgrade):
                if "enabled" in i.get_attribute("class"):
                    best2 = i           
                    break         
                                        
            for i in reversed(products):
                if "enabled" in i.get_attribute("class"):
                    best = i
                    break
            random_num = random.randint(1,2)
            if random_num == 1 :
                if best2:
                    best2.click()
            else:                
                if best:
                    best.click()
                    best.click()
                    best.click()
                    best.click()
                    best.click()
                    best.click()
                    best.click()
                    best.click()
                # print(f"Bought item: {best.get_attribute('id')}")
        except:
            print("Couldn't find cookie count or items")
                
                
        stop_time = time() + wait_time