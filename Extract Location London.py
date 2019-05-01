import json, re
import pandas as pd


keywords = ['london']
keywords = set(keywords)

with open('merged.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)

result=[]
for i in range(len(data)):
    location = data[i]['user'].get('location')
    #date = data[i].get('created_at')
    #text = data[i].get('text')
    for keyword in keywords:
        match = re.findall(keyword, location.lower())
        if match:
            dict={}
            dict['Location'] = location
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
            result.append(dict)
    #if keywords.intersection(l.lower().split()):
        #dict={}
        #dict['Date'] = d
        #dict['Location'] = l
        #result.append(dict)
            
             
print(len(result))
breakpoint()                 
#result=[]
#for row in data:
    #l = row['user']['location']
    #d = row['created_at']
    #if keywords.intersection(l.lower().split()):
        #dict={}
        #dict['Date'] = d
        #dict['Location'] = l
        #result.append(dict)
#print(dir(data[0]))
    
    
df = pd.DataFrame(result,columns=['Date','Location','Text','ID','User ID','Retweet', 'Source','Description','Entities'])
#df.to_json('Extracted London (for process).json')
df.to_json('Location London (for check).json', orient='records', lines=True)

#df.to_csv('tem2.csv', index = None, header=True, encoding='utf-8')
print(df)
with open('Location London to merge with Place London.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)
    file.close() 
