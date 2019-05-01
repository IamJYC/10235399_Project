# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:49:33 2019

@author: 祎宸
"""

import json
import pandas as pd

with open('Retweet removed.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)
    
result=[]
result.append(data[0])
#print(result)
#breakpoint()

for dict in data:
    #print(len(result))
    k=0
    for item in result:
            #print 'item'
        if dict['ID'] != item['ID']:
            k=k+1
            #continue
        else:
            break
        if k == len(result):
            #print(len(result))
            result.append(dict)
#print(k)
print(len(result))
breakpoint()
    

        #dict['Location'] = data[i].get('Location')
        #这里为了合并的格式使用了location
        #dict['Date'] = data[i].get('Date')
        #dict['Text'] = data[i].get('Text')               
        #dict['Source'] = data[i].get('Source')               
        #dict['User ID'] = data[i].get('User ID')
        #dict['ID'] = data[i].get('ID')
        #dict['Description'] = data[i].get('Description')
        #dict['Entities'] = data[i].get('Entities')
        #dict['Retweet'] = data[i].get('Retweet')                
        #result.append(dict)
        
       
        


df = pd.DataFrame(result,columns=['Date','Location','Text','ID','User ID','Retweet','Description','Entities'])
df.to_json('Identical tweets removed (for check).json', orient='records', lines=True)  
 
 
with open('Identical tweets removed.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)
    file.close()