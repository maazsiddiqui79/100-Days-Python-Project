from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ip = input("Enter job role:")
USERNAME = "maaz.irshad.siddiqui@gmail.com"
PASSWORD = "maaz1234567890MAAZ"

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)
ip.replace(" ","%20")

driver.get(url=f"https://www.linkedin.com/jobs/search/?currentJobId=4253799146&keywords={ip}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# -----------------------

def click(path):

    search_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    search_btn.click()
    
def user_cerd(path,data):
    user_op = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,path))
    )
    print("Email ip Done")
    user_op.send_keys(data)
    user_op.send_keys(Keys.ENTER)
    



# -----------------------
# Wait for and click the sign-in button
search_btn = '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button'

click(search_btn)

# Wait for and fill in the email

email_ip = '//*[@id="base-sign-in-modal_session_key"]'
user_cerd(email_ip,USERNAME)

# Wait for and fill in the password
password_ip = '//*[@id="base-sign-in-modal_session_password"]'
user_cerd(password_ip,PASSWORD)

input("Please solve the captcha manually and press Enter to continue...")

enable_easy_apply = '//*[@id="searchFilter_applyWithLinkedin"]'
click(path=enable_easy_apply)

time.sleep(2)  # Add before locating/clicking the button
save_btn_xpath = '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button/span[1]'

click(path=save_btn_xpath)


time.sleep(2)  # Add before locating/clicking the button
company_profile_xpath = '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/a'

click(path=company_profile_xpath)

follow_xpath = '/html/body/div[6]/div[4]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div/div[3]/div/div[1]/div[1]/button[1]'

click(path=follow_xpath)
print("\n✅ Task completed successfully. Your job preferences were updated on LinkedIn. Wishing you the best in your job search! 🚀")
