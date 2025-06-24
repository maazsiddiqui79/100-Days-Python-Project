from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

URL =input("Enter YouTube URL to abstract Meta Data:")
time.sleep(3)
chrome =webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome)
driver.get(url=URL)

time.sleep(3)

def extract_data(path):
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,path))
    )
    
    return element.text.replace("\n","").strip()


# Title
"title"
title = '//*[@id="title"]/h1/yt-formatted-string'
title = extract_data(path=title)

title


# Channel
"Channel"
channel = '//*[@id="text"]/a'
channel = extract_data(path=channel)

channel

# views

"views"
views ='//*[@id="info"]/span[1]'
views =extract_data(path=views)

views

# comment
"len"
# time.sleep(50)
comment = '//*[@id="count"]/yt-formatted-string/span[1]'
comment = extract_data(path=comment)

# date


"Published"
publish = '//*[@id="info"]/span[3]'
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="expand"]'))
).click()
publish = extract_data(path=publish)

publish

# des
"Description"
description1 = '//*[@id="description-inline-expander"]/yt-attributed-string/span/span[1]'
description1 = extract_data(path=description1)

description1


print(f'''
Enter the YouTube video URL: {URL}

📺 Video Metadata:
Title         : {title}
Channel       : {channel}
Views         : {views}
Comments       : {comment}
Published Date: {publish}
Description   : {description1}

''')