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
    df.to_csv('products_latest.csv', index=False, encoding='utf-8')

core_url = "https://www.myntra.com/new-trends?p="
links_list = []
for i in range(1,10):
    new_url = core_url + str(i)
    links_list.append(new_url)
scrap_latest_fashion(links_list)

