from bs4 import BeautifulSoup
import os
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time



class Rental_Web_Scraper ():
    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.data ={
            'Address': [],
            'Price': [],
            'Link': [],
        }
        self.read_file()
        self.save_data()

        
        
    def read_file(self):
        
        for i in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path,i)
            with open(file_path,'r',encoding="utf-8") as f:
                html_doc = f.read()
                
            self.extract_data(html_document=html_doc)
                
                
    def extract_data (self,html_document):
        soup = BeautifulSoup(html_document,'html.parser')
        
        try:
            # Address
            Add = soup.find('address').getText()
            
            if Add:
                self.data['Address'].append(Add.strip())
            else:
                self.data['Address'].append('N/A')
            
            # Price
            Price = soup.find('span',class_='PropertyCardWrapper__StyledPriceLine').getText()
            if Price:
                self.data['Price'].append(Price)
            else:
                self.data['Price'].append('N/A')
                
            # Link
            Link = soup.find('a',class_='property-card-link').get_attribute_list('href')
            Link = Link[0]+'.html'
            
            if Link:
                self.data['Link'].append(Link)
            else:
                self.data['Link'].append('N/A')
            
            
            
        except Exception as e:
            print('E R R O R',e)
            
            
    def save_data (self):
        data1 = pandas.DataFrame(self.data)
        for k,v in data1.iterrows():

            
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach",True)
            driver =webdriver.Chrome(options=chrome_options)
            driver.get(url="https://forms.gle/BLQq5FsVhkbBrPq7A") 
            a1 = v.Address
            print(a1)
            
            p1 = v.Price
            print(p1)
            
            l1 = v.Link
            print(l1)
            
            wait = WebDriverWait(driver, 10)
            q1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            q2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            q3 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')))

            q1.send_keys(a1)
            q2.send_keys(p1)
            q3.send_keys(l1)
            btn.click()
            time.sleep(1)
            
            driver.close()
        
        
        
            
        
        
        


    