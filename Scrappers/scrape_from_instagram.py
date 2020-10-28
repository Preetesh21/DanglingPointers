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
        players = driver.find_elements_by_xpath('//img[@class="FFVAD"]')
        for p in players:
            Links.append(str(p.get_attribute('src')))
            Descriptions.append(str(p.get_attribute('alt')))
    df = pd.DataFrame({'Product URL':Links, 'Descriptions':Descriptions}) 
    df.to_csv('products_from_instagram.csv', index=False, encoding='utf-8')

core_url = "https://www.instagram.com/explore/tags/"
hashtags = ["fashionblogger","fashionstyle","fashiontrends","styleblogger","fashionmodel","latesttrends","bollywoodfashion","latestcelebrityfashion"]
links_list = []
for tag in hashtags:
    new_url = core_url + tag
    links_list.append(new_url)
scrap_latest_fashion(links_list)




