# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:03:50 2019

@author: 祎宸
"""

import json,re
import pandas as pd

keywords2 = ['london']
keywords2 = set(keywords2)
with open('Place (for process).json', 'r', encoding='utf-8') as fd:
    tweet=json.load(fd) 
 
result2=[]
for i in range(len(tweet)):
    place_name = tweet[i]['Place'].get('full_name')
    for keyword2 in keywords2:
            match = re.findall(keyword2, place_name.lower())
            if match:
                dict={}
                dict['Location'] = place_name
                #这里为了合并的格式使用了location
                dict['Date'] = tweet[i].get('Date')
                dict['Text'] = tweet[i].get('Text')               
                dict['Source'] = tweet[i].get('Source')               
                dict['User ID'] = tweet[i].get('User ID')
                dict['ID'] = tweet[i].get('ID')
                dict['Description'] = tweet[i].get('Description')
                dict['Entities'] = tweet[i].get('Entities')
                dict['Retweet'] = tweet[i].get('Retweet')                
                result2.append(dict)
    
print(len(result2))
df2 = pd.DataFrame(result2,columns=['Date','Location','Text','ID','User ID','Retweet', 'Source','Description','Entities'])
df2.to_json('Place London (for check).json', orient='records', lines=True)  
with open('Place London to merge with Location London.json', 'w', encoding='utf-8') as file:
    json.dump(result2, file)
    file.close()  