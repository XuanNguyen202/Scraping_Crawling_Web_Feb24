# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:57:05 2023

@author: nguye
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

url='https://www.nfl.com/standings/league/2022/REG'

page=requests.get(url)
page

soup=BeautifulSoup(page.text,'lxml')

table=soup.find('table',{'summary':"Standings - Detailed View"})
table
headers=[]

for hd in table.find_all('th'):   
    title=hd.text.strip()
    headers.append(title)

df=pd.DataFrame(columns=headers)
table.find_all('td')
for r in table.find_all('tr')[1:]:
    row_data=r.find_all('td')
    row=[strg.text for strg in row_data]
    length=len(df)
    df.loc[length]=row
    
df
