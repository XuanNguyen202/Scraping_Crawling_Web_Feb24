# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:46:04 2023

@author: Xuan Nguyen
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome('D:\OneDrive - mrsnguyen\Leisure\Simple/Scraping_Crawling/chromedriver.exe')
driver.get('https://www.nike.com/vn/w/sale-3yaep')

driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/aside/div/button/i').click()

last_height=driver.execute_script('return document.body.scrollHeight')


while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    new_height=driver.execute_script('return document.body.scrollHeight')
    if new_height==last_height:
        break
    last_height=new_height
    
soup=BeautifulSoup(driver.page_source,'lxml')

product_card=soup.find_all('div',class_='product-card__body')
len(product_card)
df=pd.DataFrame({'Link':[''],'Name':[''],'Subtitle':[''],
                'Full_price':[''],'Sale_price':['']})
product_card
for product in product_card:
    link = product.find('a',class_='product-card__link-overlay').get('href')
    name = product.find('div',class_='product-card__title').text
    subtitle=product.find('div',class_='product-card__subtitle').text
    full_price=product.find('div',class_='product-price vn__styling is--striked-out css-0').text
    sale_price=product.find('div',class_='product-price is--current-price css-1ydfahe').text
    df=df.append({'Link':link,'Name':name,'Subtitle':subtitle,
              'Full_price':full_price,'Sale_price':sale_price},ignore_index=True)

df.to_csv('D:\OneDrive - mrsnguyen\Leisure\Simple\Scraping_Crawling/Undemy_crawl/Nike_scraped.csv')





























