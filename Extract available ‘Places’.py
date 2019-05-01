# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:10:08 2019

@author: 祎宸
"""

import json,re
import pandas as pd

with open('merged.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)
    #print(len(data))
    #breakpoint()

keywords1 = ['None']
keywords1 = set(keywords1)



result1=[]
for i in range(len(data)):
    place = data[i].get('place')
    for keyword1 in keywords1:
            match = re.findall(keyword1, str(place))
            if not match:
                dict={}   
                dict['Place'] = place
                dict['Date'] = data[i].get('created_at')
                dict['Text'] = data[i].get('text')
                #dict['Place'] = data[i].get('place')
                dict['Source'] = data[i].get('source')
                #dict['Retweeted'] = data[i].get('retweeted')
                #dict['Rt times'] = data[i].get('retweet_count')
                dict['User ID'] = data[i]['user'].get('id_str')
                dict['ID'] = data[i].get('id_str')
                dict['Description'] = data[i]['user'].get('description')
                #dict['Derived'] = data[i]['user'].get('derived')
                dict['Entities'] = data[i].get('entities')
                dict['Retweet'] = data[i].get('retweeted_status')
                #dict['Quote'] = data[i].get('quoted_status')
                result1.append(dict)
    
print(len(result1))
df1 = pd.DataFrame(result1,columns=['Date','Place','Text','ID','User ID','Retweet', 'Source','Description','Entities'])
df1.to_json('Place (for check).json', orient='records', lines=True)  
#df1.to_json('Place (for process).json') 
 
with open('Place (for process).json', 'w', encoding='utf-8') as file:
    json.dump(result1, file)
    file.close()             















#keywords = ['null']
#keywords = set(keywords)

#result=[]
#for i in range(len(data)):
    #place = data[i].get('place')
    #match = re.findall(keyword, place)
    #breakpoint()
    #try:
        #for keyword in keywords:
            #match = re.findall(keyword, place)
    #except TypeError:
        #continue
    #else:
       # if match:   
            #dict={}
            #dict['Place'] = place
            #result.append(dict)
       
        
             
        
            
#print(len(result))
#breakpoint()
#df = pd.DataFrame(result,columns=['Place'])
#df.to_json('Place (for check).json', orient='records', lines=True)
    

            
    
    



    
    
    
    


