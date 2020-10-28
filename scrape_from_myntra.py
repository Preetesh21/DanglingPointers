from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

def scrap_latest_fashion(links_list):
    Links=[] 
    Descriptions=[] 
    driver = webdriver.Chrome("/home/garima/chromedriver")
    for url in links_list:
        driver.get(url)
        players = driver.find_elements_by_xpath('//img[@class="img-responsive"]')
        for p in players:
            Links.append(str(p.get_attribute('src')))
            Descriptions.append(str(p.get_attribute('title')))
    df = pd.DataFrame({'Product URL':Links, 'Descriptions':Descriptions}) 
    df.to_csv('products.csv', index=False, encoding='utf-8')

keywords = ["latest","trending","bestselling"]   
gender = ["women","men","kids","boys","girls"] 
fashion_list = ["tops","trousers","jeans","shorts","tshirts","kurtas","shirts","pants"]
links_list = []
core_url = "https://www.myntra.com/"

for key in keywords :
    for gen in gender:
        for style in fashion_list:
            new_url = core_url +key+gen+style
            links_list.append(new_url)

core_url = "https://www.myntra.com/new-trends?p="
for i in range(1,5):
    new_url = core_url + str(i)
    links_list.append(new_url)
scrap_latest_fashion(links_list)
