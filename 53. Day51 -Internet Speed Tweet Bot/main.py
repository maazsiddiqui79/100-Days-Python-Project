from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver =webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.speedtest.net/")


btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]'))
).click()

time.sleep(40)


try:
    add_x_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[8]/div/a'))
    ).click()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
except Exception as e:
    print("Element not found: ",e)

download_speed_xpath ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
upload_speed_xpath ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
result_id_xpath ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[1]/div/div/div[2]'
service_provider_xpath ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[2]/div[2]/a'
unit_xpath= '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[1]/span'


download_speed = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,download_speed_xpath))
    ).text
upload_speed = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,upload_speed_xpath))
    ).text
result_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,result_id_xpath))
    ).text
service_provider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,service_provider_xpath))
    ).text
unit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,unit_xpath))
    ).text


driver.execute_script("window.open('https://x.com/home','_blank');")
driver.switch_to.window(driver.window_handles[1])



# Set up the WebDriver (use your path)


# Open Twitter
time.sleep(5)

# Enter username
username_input = driver.find_element(By.NAME, "text")
username_input.send_keys("siddiquimaazzz")
username_input.send_keys(Keys.RETURN)
time.sleep(3)
# Enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("you password")
password_input.send_keys(Keys.RETURN)
time.sleep(3)

msg =f'''
📡 Internet Speed Test Result
🔻 Download Speed: {download_speed} {unit}
🔺 Upload Speed: {upload_speed} {unit}
🆔 Result ID: {result_id}
📶 Provider: {service_provider}

Despite paying a premium, this is the speed I'm getting. Totally unacceptable!
Please fix this immediately, @{service_provider.lower().replace(" ","")}
#InternetSpeed #SlowInternet #FixIt
'''


time.sleep(5)
user_ip = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
print(msg)
time.sleep(2)
user_ip.send_keys(f'''
Download: {download_speed} {unit} | Upload: {upload_speed} {unit}  
Provider: {service_provider} | Result ID: {result_id}  
Paying premium, getting this? Unacceptable.  
Fix this ASAP, @{service_provider.lower().replace(" ","")}  
#InternetSpeed #SlowInternet ''')
time.sleep(5)

time.sleep(2)
btn = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
# btn = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]'))
# )

btn.click()

# Close browser when done
# driver.quit()
