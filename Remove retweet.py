# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:55:53 2019

@author: 祎宸
"""

import json, re
import pandas as pd

with open('merged for London.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)
    print(len(data))
    breakpoint()

keywords = ['created_at']
keywords = set(keywords)



result=[]
for i in range(len(data)):
    retweet = data[i].get('Retweet')
    for keyword in keywords:
            match = re.findall(keyword, str(retweet))
            if not match:
                dict={}
                dict['Location'] = data[i].get('Location')
                #这里为了合并的格式使用了location
                dict['Date'] = data[i].get('Date')
                dict['Text'] = data[i].get('Text')               
                dict['Source'] = data[i].get('Source')               
                dict['User ID'] = data[i].get('User ID')
                dict['ID'] = data[i].get('ID')
                dict['Description'] = data[i].get('Description')
                dict['Entities'] = data[i].get('Entities')
                dict['Retweet'] = retweet                
                result.append(dict)
    
print(len(result))
breakpoint()
df = pd.DataFrame(result,columns=['Date','Location','Text','ID','User ID','Retweet', 'Source','Description','Entities'])
df.to_json('Retweet removed (for check).json', orient='records', lines=True)  
#df1.to_json('Place (for process).json') 
 
with open('Retweet removed.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)
    file.close()