# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:05:54 2019

@author: 祎宸
"""

import json,re,string
from nltk import ngrams, FreqDist
import matplotlib.pyplot as plt
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import pandas as pd
from collections import defaultdict
from wordcloud import WordCloud, STOPWORDS
import preprocessor as p


with open('extract_Feb.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)
    


def get_ngrams(text, n ):
    n_grams = ngrams(text, n)
    return [''.join(grams) for grams in n_grams]

    
Word_cloud_stopwords = set(STOPWORDS)
Word_cloud_stopwords.add('nhttps')
Word_cloud_stopwords.add('u2066')
Word_cloud_stopwords.add('u2069')
Word_cloud_stopwords.add('amp')
Word_cloud_stopwords.add('RT')


def show_wordcloud(tt, title = None):
    wordcloud = WordCloud(
        background_color='black',
        stopwords=Word_cloud_stopwords,
        max_words=200,
        max_font_size=50,
        width=500, height=309,
        scale=3.0,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(tt))

    fig = plt.figure(1, figsize=(20, 12.36))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)
    plt.imshow(wordcloud)
    plt.savefig("WC_Negative.png", format="png")
    #plt.show() 
def clean_tweets(text):    
    stopwords_english = stopwords.words('english')
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(text)
    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and # remove stopwords
                word not in string.punctuation): # remove punctuation
            tweets_clean.append(word)
                                                         
    return tweets_clean
    
merged = defaultdict(list)
for myd in data:
    for k, v in myd.items():
        merged[k].append(v)

tweet_text = str(merged['Text'])
cleaned = p.clean(tweet_text)

#print(cleaned)
#print(tweet_text)
#tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
#wc_tokens = tokenizer.tokenize(cleaned)

            
air_pollution_removed = cleaned.replace('air pollution', '')
Air_pollution_removed = air_pollution_removed.replace('Air pollution', '')
air_quality_removed = Air_pollution_removed.replace('air quality', '')
Air_qualiiy_removed = air_quality_removed.replace('Air quality', '')
Air_Qualiiy_removed = Air_qualiiy_removed.replace('Air Quality', '')
Air_Pollution_removed = Air_Qualiiy_removed.replace('Air Pollution', '')        
dot_removed = Air_Pollution_removed.replace('…', '')
quote_removed = dot_removed.replace('’', '')
nhttps_removed = quote_removed.replace('nhttps', '')
four_removed =  nhttps_removed.replace(':/', '')
three_removed = four_removed.replace('“', '')
two_removed = three_removed.replace('‘', '')
one_removed = two_removed.replace('”', '')
o_removed = one_removed.replace('...', '')
i_removed = o_removed.replace('–', '')
asthma_removed = i_removed.replace('asthma', '')
haze_removed = asthma_removed.replace('haze', '')
smog_removed = haze_removed.replace('smog', '')
Smog_removed = smog_removed.replace('Smog', '')
Haze_removed = Smog_removed.replace('Haze', '')
Asthma_removed = Haze_removed.replace('Asthma','')
last_removed = Asthma_removed.replace('\\n','')
final_removed = last_removed.replace('u2066','')
fianlly_remvoed = final_removed.replace('u2069','')
      #u2066
#print(keywords_removed)
#show_wordcloud(fianlly_remvoed)

unigrams = get_ngrams(clean_tweets(fianlly_remvoed),1)
bigrams = get_ngrams(clean_tweets(fianlly_remvoed),2)
trigrams = get_ngrams(clean_tweets(fianlly_remvoed),3)


plt.figure(figsize=(10,3))
#plt.savefig('unigram.png',dpi=200)
FreqDist(unigrams).plot(50,cumulative=False)



plt.figure(figsize=(12, 4))
FreqDist(bigrams).plot(50,cumulative=False,)

plt.figure(figsize=(15, 5))
FreqDist(trigrams).plot(50,cumulative=False,)



#print(FreqDist(unigrams).most_common(50))
#print(FreqDist(bigrams).most_common(50))
#print(FreqDist(trigrams).most_common(50))

