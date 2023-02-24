# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:12:38 2023

@author: nguye

Chapter 5 Scraping Table
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.worldometers.info/world-population/'

page=requests.get(url)
page
soup=BeautifulSoup(page.text,'lxml')
soup

table=soup.find('table',class_='table table-striped table-bordered table-hover table-condensed table-list')
table

table.find_all('th')
headers=[]
for hd in table.find_all('th'):
    title=hd.text
    headers.append(title)
headers

df=pd.DataFrame(columns=headers)

for r in table.find_all('tr')[1:]:
    row_data=r.find_all('td')
    row=[tr.text for tr in row_data]
    length=len(df) #so dong- row
    df.loc[length]=row
    
lenght=len(df)
print(lenght)

df.to_csv('D:/OneDrive - mrsnguyen/Leisure/Simple/Scraping_Crawling/Undemy_crawl/table_scraped.csv')


