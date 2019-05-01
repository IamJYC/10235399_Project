# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:46:49 2019

@author: 祎宸
"""
import collections
from nltk.metrics import *
from nltk.classify import NaiveBayesClassifier, MaxentClassifier, SklearnClassifier
from sklearn.svm import LinearSVC, SVC
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import json,re,string
from nltk import ngrams, FreqDist
import matplotlib.pyplot as plt
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import twitter_samples
from random import shuffle
from nltk import classify
from nltk import NaiveBayesClassifier, MaxentClassifier, SklearnClassifier
import pandas as pd
from collections import defaultdict



with open('merged_keywords.json', 'r', encoding='utf-8') as fd:
    data=json.load(fd)
tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
stopwords_english = stopwords.words('english')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])
 
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])
 
emoticons = emoticons_happy.union(emoticons_sad)

    
def clean_tweets(tweet):
    tweet = re.sub(r'\$\w*', '', tweet) 
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)    
    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet) 
    tweets_clean = []    
    for word in tweet_tokens:
        if (word not in stopwords_english and # remove stopwords
              word not in emoticons and # remove emoticons
                word not in string.punctuation): # remove punctuation
            #tweets_clean.append(word)
            stem_word = stemmer.stem(word) # stemming word
            lemmatized_word = lemmatizer.lemmatize(stem_word)
            tweets_clean.append(lemmatized_word)                                             
    return tweets_clean

def bag_of_words(tweet):
    words = clean_tweets(tweet)
    words_dictionary = dict([word, True] for word in words)    
    return words_dictionary

pos_tweets = twitter_samples.strings('positive_tweets.json') 
neg_tweets = twitter_samples.strings('negative_tweets.json') 
all_tweets = twitter_samples.strings('tweets.20150430-223406.json')

pos_tweets_set = []
for tweet in pos_tweets:
    pos_tweets_set.append((bag_of_words(tweet), 'pos'))
neg_tweets_set = []
for tweet in neg_tweets:
    neg_tweets_set.append((bag_of_words(tweet), 'neg'))

shuffle(pos_tweets_set)
shuffle(neg_tweets_set)
 
test_set = pos_tweets_set[:2500] + neg_tweets_set[:2500]
train_set = pos_tweets_set[2500:] + neg_tweets_set[2500:]
#train_set = pos_tweets_set + neg_tweets_set

ME_classifier = MaxentClassifier.train(train_set, 'GIS', trace=0, encoding=None, labels=None, gaussian_prior_sigma=0, max_iter = 1)
NB_classifier = NaiveBayesClassifier.train(train_set)
SVM_classifier = SklearnClassifier(LinearSVC(), sparse=False)
SVM_classifier.train(train_set)

#ME_accuracy = classify.accuracy(ME_classifier, test_set)
#NB_accuracy = classify.accuracy(NB_classifier, test_set)
#SVM_accuracy = classify.accuracy(SVM_classifier, test_set)
#print(ME_accuracy, NB_accuracy, SVM_accuracy)


actual_set = defaultdict(set)
predicted_set = defaultdict(set)
 
 
for index, (feature, actual_label) in enumerate(test_set):
    actual_set[actual_label].add(index) 
    predicted_label = NB_classifier.classify(feature) 
    predicted_set[predicted_label].add(index)
    
accuracy = classify.accuracy(NB_classifier, test_set)
pos_fmeasure = f_measure(actual_set['pos'], predicted_set['pos'])
neg_fmeasure = f_measure(actual_set['neg'], predicted_set['neg'])

print ('accuracy:', accuracy)
print ('f-measure', (pos_fmeasure + neg_fmeasure)/2)





                                                                












def Maximum_Entropy():
    result=[]
    for row in data:
        my_tweet = row['Text']
        my_tweet_set =bag_of_words(my_tweet)
        sentiment = ME_classifier.classify(my_tweet_set)
        item={}
        item['Text']=row['Text']
        item['Date']=row['Date']
        item['Sentiment']=sentiment
        result.append(item)

    positivetweets = [tweet for item in result if item['Sentiment'] == 'pos']
    negativetweets = [tweet for item in result if item['Sentiment'] == 'neg']
    Positivepercentage = (len(positivetweets)/len(result))
    Negativepercentage = (len(negativetweets)/len(result))
    print('Maximum_Entropy:'"Positive: {:.2%}".format(Positivepercentage), "Negative: {:.2%}".format(Negativepercentage))
    #with open('Maximum_Entropy_result.json', 'w', encoding='utf-8') as file:
        #json.dump(result, file)
        #file.close()
        #df = pd.DataFrame(result,columns=['Date','Text','Sentiment'])                               
        #df.to_json('Maximum_Entropy_result (for check).json', orient='records', lines=True)

def NaiveBayes():
    result=[]
    for row in data:
        my_tweet = row['Text']
        my_tweet_set =bag_of_words(my_tweet)
        sentiment = NB_classifier.classify(my_tweet_set)
        item={}
        item['Text']=row['Text']
        item['Date']=row['Date']
        item['Sentiment']=sentiment
        result.append(item)

    positivetweets = [tweet for item in result if item['Sentiment'] == 'pos']
    negativetweets = [tweet for item in result if item['Sentiment'] == 'neg']
    Positivepercentage = (len(positivetweets)/len(result))
    Negativepercentage = (len(negativetweets)/len(result))
    print('Naive Bayes:'"Positive: {:.2%}".format(Positivepercentage), "Negative: {:.2%}".format(Negativepercentage))
    #with open('Naive_Bayes_result.json', 'w', encoding='utf-8') as file:
        #json.dump(result, file)
        #file.close()
        #df = pd.DataFrame(result,columns=['Date','Text','Sentiment'])                               
        #df.to_json('Naive_Bayes_result (for check).json', orient='records', lines=True)

def SVM():
    result=[]
    for row in data:
        my_tweet = row['Text']
        my_tweet_set =bag_of_words(my_tweet)
        sentiment = SVM_classifier.classify(my_tweet_set)
        item={}
        item['Text']=row['Text']
        item['Date']=row['Date']
        item['Sentiment']=sentiment
        result.append(item)

    positivetweets = [tweet for item in result if item['Sentiment'] == 'pos']
    negativetweets = [tweet for item in result if item['Sentiment'] == 'neg']
    Positivepercentage = (len(positivetweets)/len(result))
    Negativepercentage = (len(negativetweets)/len(result))
    print('SVM:'"Positive: {:.2%}".format(Positivepercentage), "Negative: {:.2%}".format(Negativepercentage))
    #with open('SVM_result.json', 'w', encoding='utf-8') as file:
        #json.dump(result, file)
        #file.close()
        #df = pd.DataFrame(result,columns=['Date','Text','Sentiment'])                               
        #df.to_json('SVM_result (for check).json', orient='records', lines=True)
#SVM()
#NaiveBayes()
#Maximum_Entropy()