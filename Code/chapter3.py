"""
Created on Wed Feb 22 22:20:41 2023

@author: nguye
"""

import requests
from bs4 import BeautifulSoup

url='https://webscraper.io/test-sites/e-commerce/allinone/computers'
page=requests.get(url)
page

soup=BeautifulSoup(page.text,'lxml')
soup.header
soup

#Tags
soup.header
soup.div

#Navigable Strings
tag=soup.header.p
tag.string
tag.header.p.string


#Attributes
tag=soup.header.a
tag.attrs
tag['data-toggle']
tag['attribute']='this is a attribute'
tag.attrs

##section4_18
import requests
from bs4 import BeautifulSoup

url='https://webscraper.io/test-sites/e-commerce/allinone/phone/touch'

page=requests.get(url)
page

soup=BeautifulSoup(page.text,'lxml')
soup

#find
soup.find('header')
soup.headers.attrs

soup.find('div',{'class':'container test-site'})
soup.find_all('h4',{'class':'pull-right price'})
soup.find_all('h4',class_='pull-right price')


soup.find_all('a',class_='title')
soup.find_all('p',class_ ='pull-right')

soup.find_all(['h4','p'])

#id
soup.find_all(id=True)


soup.find_all(string='Iphone') ###errror

import re

soup.find_all(string=re.compile('Nok')) #errrorr
soup.find_all(class_=re.compile('pull'))

soup.find_all('p',class_=re.compile('pull'))

soup.find_all('p',class_=re.compile('pull'),limit=2)

# find_all part3
product_name=soup.find_all('a',class_='title')
product_name

prices=soup.find_all('h4',class_='pull-right price')
prices

reviews=soup.find_all('h4',class_=re.compile('pull'))
reviews

descriptions=soup.find_all('p',class_='description')
descriptions
# =============================================================================
# description=soup.find('p',class_='description')
# description.text -- chi ap dung voi find
# =============================================================================
 
product_name_list=[]
for product in product_name:
    name=product.text
    product_name_list.append(name)

prices_list=[]
for price in prices:
    p=price.text
    prices_list.append(p)

reviews_list=[]
for review in reviews:
    r=review.text
    reviews_list.append(r)

descriptions_list=[]
for description in descriptions:
    d=description.text
    descriptions_list.append(d)

import pandas as pd

table=pd.DataFrame({'Product_Name':product_name_list,
                    'Description':descriptions_list,
                    'Price':prices_list,
                    'Reviews':reviews_list})
table


#extracted data from nested HTML tags
boxes=soup.find_all('div',class_='col-sm-4 col-lg-4 col-md-4')
boxes

len(boxes)

boxes=soup.find_all('div',class_='col-sm-4 col-lg-4 col-md-4')[2]
boxes
boxes.find('a').text
boxes.find('p',class_='description').text

box2=soup.find_all('ul',class_='nav',id='side-menu')[0]
box2.find_all('li')[1]


#1. remember to import the HTML into python
import requests
from bs4 import BeautifulSoup

url='https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'
page=requests.get(url)
soup=BeautifulSoup(page.text,'lxml')

#2. price of the stock
prices=soup.find('bg-quote', class_='value')
prices.text
# =============================================================================
# prices_list=[]
# for price in prices:
#     p=price.text
#     prices_list.append(p)
# prices_list
# =============================================================================
    

#3. closing price of the stock

closing_prices=soup.find('td',class_='table__cell u-semi')
closing_prices.text
# =============================================================================
# closing_prices_list=[]
# for cl_price in closing_prices:
#     clp=cl_price.text
#     closing_prices_list.append(clp)
# closing_prices_list

# =============================================================================
    
#4. 52 week range (lower, upper)
# =============================================================================
# week52_range_lower=soup.find_all('span',class_='primary')[0].text
# week52_range_lower
# =============================================================================

nested = soup.find('mw-rangebar',class_='element element--range range--yearly')
nested

lower=nested.find_all('span',class_='primary')[0].text
lower
upper=nested.find_all('span',class_='primary')[1].text
upper

#5. analyst rating
rating=soup.find('li',class_='analyst__option active').text
rating


