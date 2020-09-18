# I think we may need database software to help the data storage and extract which is efficient.
# If neccessary, please download the mongodb from the offical website: https://www.mongodb.com/
import json
import pymongo
import pandas as pd
import numpy as np
import re
stop_words = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during',
              'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
              'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from',
              'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their',
              'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before',
              'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that',
              'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself',
              'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't',
              'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than')

np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)

#display all of the columns
pd.set_option('display.max_columns', None)
#display all of the rows
pd.set_option('display.max_rows', None)
from collections import Counter

collection = None
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # get a database
    db = client['assign1']
    # create and the the collection
    collection = db['tweeta']

except Exception as e:
    print(e)

# tweets to list
tweets_list = []


#created_at text user.id user.name user.followers_count user.friends_count
# place.country place.full_name retweet_count favorite_count lang
top_tweets = collection.find({'lang':'en', 'place.country':'United States'},
                             {'_id':0,'created_at':1,'text':1, 'user.id':1, 'user.name':1, 'user.followers_count':1,
                              'user.friends_count':1, 'place.full_name':1, 'retweet_count':1, 'favorite_count':1})


for i in top_tweets:
    # print(i['user']['id'])
    tweets_list.append([i['created_at'], i['text'], i['user']['id'], i['user']['name'], i['user']['followers_count'],
                        i['user']['friends_count'], i['place']['full_name'], i['retweet_count'], i['favorite_count']])
# use top 5000 tweets for coding test
# removing the foreign tweets (outside USA)
# removing tweets in different languages
# for i in top_tweets:
#     tweets_list.append()

# 9 attris
attri = ['created_at', 'text', 'user_id', 'user_name', 'user_followers_count', 'user_friends_count',
         'place_full_name', 'retweet_count', 'favorite_count']
data = pd.DataFrame(tweets_list, columns=attri)

print(data.shape)
# print(data)
print(data.iloc[0,:])
# data.to_csv('out.csv',index=True)

print('------------------')


# removing URL links (http or www pattern) and to lower case
def rm_URL_lowcase(record: str) -> str:
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    sub_record = re.sub(regex, '', record).lower()
    return sub_record

print(rm_URL_lowcase("own mouth, and they do Continually https://t.co/pKSQM8yikm"))


# removing hashtags and @
def rm_hashtags(record: str) -> str:
    sub_record = re.sub(r'@|#', '', record)
    return sub_record

print(rm_hashtags("own mouth, and they @do #Continually https://t.co/pKSQM8yikm"))

# removing repeating letters (i.e. awesooome to awesome,
def rm_repeat(record: str) -> str:
    pass #TODO

# removing punctuation
def rm_punctuation(record: str) -> str:
    s = re.sub(r'[^\w\s]', '', record)
    return s


# removing stopwords - i.e. the, a, an, he\
def rm_stopwords(record: str) -> str:
    words = list(record.split(' '))
    filtered_sentence = ' '.join([w for w in words if not w in stop_words])
    return filtered_sentence

print('++++')
print(rm_stopwords("own mouth, a and they @do the #Continually https://t.co/pKSQM8yikm"))

# removing short words - those with less than 3 letters ???
def rm_shortwords(record: str) -> str:
    pass

for i in range(data.shape[0]):
    data.iloc[i, 1] = rm_URL_lowcase(data.iloc[i,1])
    data.iloc[i, 1] = rm_hashtags(data.iloc[i, 1])
    data.iloc[i, 1] = rm_punctuation(data.iloc[i, 1])
    data.iloc[i, 1] = rm_stopwords(data.iloc[i, 1])
    # print(data.iloc[i, 1])

data.to_csv('outa.csv',index=True)

# removing HTML decoding - using BeautifulSoup (cases like:  &amp - tweet 9)
# check cases with more than 140 characters - as this is the twitter max of characters and why we have tweets exceeding this limit
# lemmatizing the words - which is i.e. changing words in the third person to first or changing verbs to the infinitive(basic) form?
# some negation handling - how to keep the negation meaning?
# replacing or removing emojis - if there are any

# removing tweets that are empty after cleaning

# dividing into validation, test and training sets
