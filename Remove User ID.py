# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:16:53 2019

@author: 祎宸
"""
import json
import pandas as pd

with open('Identical tweets removed.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)
    #print(len(data))
    #breakpoint()
keywords = ['46686954','90386445','394037460','40902068','908342755159629824','3039756115',
            '845553265','19827010','16973333','20329672','87818409','550901295','34906869',
            '2507377250','20582958','2978275395','117489156','2842505068','2220031111',
            '38142380','2220067358','449148677','39526753','970392881776267265','19397942',
            '2748867979','741643957407494144','16558943','89711639','81972515','244513778',
            '21387239','14700117','6107422','144461413','558522993','563614918','563612260',
            '562780227','562698688','550026166','560944015']


#print(keywords)
#breakpoint()
result=[]
for dict in data:
    k=0
    for keyword in keywords:
        
        if dict['User ID'] != keyword:
            k=k+1                                    
        else:
            break
        if k == len(keywords):            
            result.append(dict)
            
    
print(k)    
print(len(result))
breakpoint()
df = pd.DataFrame(result,columns=['Date','Location','Text','ID','User ID','Retweet','Description','Entities'])
df.to_json('User ID removed (for check).json', orient='records', lines=True)  
#df1.to_json('Place (for process).json') 
 
with open('User ID removed.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)
    file.close()
#for i in range(len(data)):
    #user_id = data[i].get('User ID')
    #for keyword in keywords:
        #match = re.findall(keyword, user_id)
        #if match:   
            #dict={}
            #dict['Location'] = data[i].get('Location')
                #这里为了合并的格式使用了location
            #dict['Date'] = data[i].get('Date')
            #dict['Text'] = data[i].get('Text')               
                #dict['Source'] = data[i].get('Source')               
            #dict['User ID'] = user_id
            #dict['ID'] = data[i].get('ID')
            #dict['Description'] = data[i].get('Description')
            #dict['Entities'] = data[i].get('Entities')
            #dict['Retweet'] = data[i].get('Retweet')                
            #result.append(dict)
    
#print(len(result))
#breakpoint()
             
