from curl_cffi import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
# from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import csv

def get_data( request ):


    chrome_options = Options()
    chrome_options.add_argument("--start-maximized") 
    chrome_options.add_argument("--disable-notifications") 
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    cookies_file = 'cookies'
    with open(cookies_file, 'r') as file:
        cookies = json.load(file)
        print("Cookies loaded successfully.")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.amazon.com")
    for cookie in cookies:
        if "sameSite" in cookie:
            del cookie["sameSite"]
        driver.add_cookie(cookie)
    driver.refresh()
    driver.get('https://www.amazon.com')
    time.sleep(6)
    inputElement = driver.find_element(By.NAME, 'field-keywords')
    inputElement.send_keys('controller for pc wireless')
    time.sleep(5)
    inputElement.send_keys(Keys.RETURN)
    time.sleep(7)
    
    dataset = []
    while True:
            items = driver.find_elements(By.CSS_SELECTOR, ".s-result-item.s-asin")
            for item in items:
                try:
                    title = item.find_element(By.CLASS_NAME, 'a-size-medium').text
                except: 
                    title = 'No title'
                try:
                    price = item.find_element(By.CLASS_NAME, 'a-price').text
                except:
                    price = 'No price'
                try:
                    link  = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')
                except:
                    link = 'No link'
                
                dataset.append({
                    'title': title,
                    'price': price.replace("\n", "."),
                    'link': link
                })
                if len(dataset) == request:
                    print(f"total items {len(dataset)} from {request} requested")
                    with open('dataset.json', 'w') as file:
                        json.dump(dataset, file)
                    save_document()
                    input("Press enter to exit...")
                    driver.quit()
                    exit()
                    
            next = driver.find_element(By.CLASS_NAME, 's-pagination-next')
            if next.is_enabled():
                next.click()  
                time.sleep(5)

def save_document( ):
    
    with open("dataset.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    
    output =  f"{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"
    with open(output, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader() 
        writer.writerows(data)
    
    print(f"Document saved as {output}")

if __name__ == '__main__':
    get_data( 50 )
    
