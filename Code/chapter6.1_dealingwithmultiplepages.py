# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:05:38 2023

@author: nguye
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


url='https://www.airbnb.com/s/Hanoi--Vietnam/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Hanoi%2C%20Vietnam&place_id=ChIJoRyG2ZurNTERqRfKcnt_iOc&date_picker_type=calendar&checkin=2023-03-15&checkout=2023-03-22&source=structured_search_input_header&search_type=autocomplete_click'

page=requests.get(url)
page

soup=BeautifulSoup(page.text,'lxml')
soup

df=pd.DataFrame({'Links':[''], 'Title':[''], 'Details':[''], 
                 'Price/Day':[''],'TotalPrice':[''],'Rating':['']})

while True:
    
    postings=soup.find_all('div',class_='c4mnd7m dir dir-ltr')
    for post in postings:
        try: # edit error in blank rating cases
            link=post.find('a',class_='l1j9v1wn bn2bl2p dir dir-ltr').get('href')
            link_full = 'https://www.airbnb.com'+link
            title=post.find('div', class_="t1jojoys dir dir-ltr" ).text
            price = post.find('span', class_="a8jt5op dir dir-ltr").text
            total_price=post.find_all('span', class_="a8jt5op dir dir-ltr")[1].text
            rating=post.find('span',class_="r1dxllyb dir dir-ltr").text
            details=post.find_all('div',class_="f15liw5s s1cjsi4j dir dir-ltr")[1].text
            
            df=df.append({'Links':link_full, 'Title':title, 'Details':details, 
                             'Price/Day':price,'TotalPrice':total_price,'Rating':rating},ignore_index=True)
        except:
            pass
        
# 1 error when scrape at last page --> run last code. --> completed scrape
    next_page=soup.find('a',{'aria-label':'Next'}).get('href')
    next_page_full='https://www.airbnb.com'+next_page
    next_page_full
    
    url=next_page_full
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'lxml')
    

df.to_csv('D:\OneDrive - mrsnguyen\Leisure\Simple\Scraping_Crawling/Undemy_crawl/room_scrapped_onAirbnb.csv')

