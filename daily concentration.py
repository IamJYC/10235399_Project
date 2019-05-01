# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:45:50 2019

@author: 祎宸
"""



from datetime import datetime
import matplotlib.dates as mdates
import matplotlib as mpl
import json, re
import pandas as pd
from pandas import Series
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.ticker as ticker

with open('Naive_Bayes_result.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)
df3 = pd.read_csv("cleaning.csv")
df3['Date'] = pd.to_datetime(df3['Date'])

def Process_tweets():            
    df1 = pd.DataFrame.from_dict(data, orient='columns')
    remove_ms = lambda x:re.sub("\+\d+\s","",x)
    mk_dt = lambda x:datetime.strptime(remove_ms(x), "%a %b %d %H:%M:%S %Y")        
    us_form = lambda x:"{:%Y/%m/%d}".format(mk_dt(x))              
    formatted = df1.Date.apply(us_form)
    formatted_count = formatted.value_counts().sort_index()
    #print(formatted_count)
    df2 = formatted_count.rename_axis('Date').reset_index(name='counts')
    df2['Date'] = pd.to_datetime(df2['Date'])
    return df2
    
def merge_dates():
    merged_date=pd.merge(Process_tweets(), df3, on='Date',how='inner')
    merged_date["Date"] = pd.to_datetime(merged_date['Date'])
    merged_date.sort_values(by=['Date'])
    #merged_date['Month'] = merged_date['Date'].dt.month
    #print(merged_date['Month'])
    return merged_date
df = merge_dates()
df['PM2.5/ugm-3']=df['PM2.5/ugm-3'].astype(float)
df['CO/mgm-3']=df['CO/mgm-3'].astype(float)
df['NO/ugm-3']=df['NO/ugm-3'].astype(float) 
df['NO2/ugm-3']=df['NO2/ugm-3'].astype(float)
df['NOX as NO2/ugm-3']=df['NOX as NO2/ugm-3'].astype(float)
df['O3/ugm-3']=df['O3/ugm-3'].astype(float)
df['SO2/ugm-3']=df['SO2/ugm-3'].astype(float)

#ax = df.plot(x="Date", y="PM2.5/ugm-3", legend="PM2.5/ugm-3")
Oct = df[df['Date'].dt.month == 10]
Nov = df[df['Date'].dt.month == 11]
Dec = df[df['Date'].dt.month == 12]
Jan = df[df['Date'].dt.month == 1]
Feb = df[df['Date'].dt.month == 2]

fig = plt.figure(figsize=(6,3.708))
ax = fig.add_subplot(111)
wow1 = ax.plot(Feb['Date'], Feb['DAQI'], '-', label = 'DAQI')
ax2 = ax.twinx()
wow2 = ax2.plot(Feb['Date'], Feb['counts'], '-r', label = 'the total tweets')
wow = wow1 + wow2
wows = [w.get_label() for w in wow]
ax.legend(wow, wows, loc=0)
ax.grid()
ax.set_xlabel("Date")
ax.set_ylabel("Daily Air Quality Index Value")
#ax.set_ylabel(r"PM10/μgm-3")
ax2.set_ylabel("Daily frequency of tweets")


#plt.xticks(pd.date_range('2018-11-01','2018-11-30'),rotation=90)
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.gcf().autofmt_xdate()
date_format = mpl.dates.DateFormatter("%d/%m/%Y")
ax.xaxis.set_major_formatter(date_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
fig.autofmt_xdate()
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%1.1f'))
plt.show()
#plt.savefig('high_negative_DAQI')

#ax = Nov.plot(x="Date", y="DAQI", label='DAQI')
#ax2 = ax.twinx()
#Nov.plot(x="Date", y="counts", ax=ax2, color='r', label='Daily frequency of tweets')


#print('October:', pearsonr(Oct['counts'], Oct['PM10/ugm-3']))
#print('November:', pearsonr(Nov['counts'], Nov['PM10/ugm-3']))
#print('December:', pearsonr(Dec['counts'], Dec['PM10/ugm-3']))
#print('January:', pearsonr(Jan['counts'], Jan['PM10/ugm-3']))
#print('February:', pearsonr(Feb['counts'], Feb['PM10/ugm-3']))

#ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax4 = ax.twinx()
#ax5 = ax.twinx()
#ax6 = ax.twinx()
#ax7 = ax.twinx()
#ax8 = ax.twinx()

#df.plot(x="Date", y="PM10/ugm-3", legend="PM10/ugm-3", color = 'r')
#df.plot(x="Date", y="CO/mgm-3",legend="CO/mgm-3", color = 'y')
#df.plot(x="Date", y="NO/ugm-3", legend="NO/ugm-3", color = 'g')
#df.plot(x="Date", y="NO2/ugm-3", legend="NO2/ugm-3", color = 'b')
#df.plot(x="Date", y="NOX as NO2/ugm-3", legend="NOX as NO2/ugm-3")
#df.plot(x="Date", y="O3/ugm-3", legend="O3/ugm-3")
#df.plot(x="Date", y="SO2/ugm-3", legend="SO2/ugm-3")
#df3.plot(x="Date", y="DAQI", legend="Daily Air Quality Index")


