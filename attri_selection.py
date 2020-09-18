# I think we may need database software to help the data storage and extract which is efficient.
# If neccessary, please download the mongodb from the offical website: https://www.mongodb.com/
import json
import pymongo
import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)

# display all of the columns
pd.set_option('display.max_columns', None)
# display all of the rows
pd.set_option('display.max_rows', None)
from collections import Counter

collection = None
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # get a database
    db = client['assign1']
    # create and the the collection
    collection = db['tweet']

except Exception as e:
    print(e)

# tweets to list
tweets_list = []

# created_at text user.id user.name user.followers_count user.friends_count
# place.country place.full_name retweet_count favorite_count lang
top_tweets = collection.find({},
                             {'_id': 0, 'created_at': 1, 'text': 1, 'user.id': 1, 'user.name': 1,
                              'user.followers_count': 1,
                              'user.friends_count': 1, 'place.full_name': 1, 'place.country':1, 'lang':1, 'retweet_count': 1, 'favorite_count': 1})

for i in top_tweets:

    if len(i) < 7:
        i['place'] = {}
        i['place']['country'] = 'unknown'
        i['place']['full_name'] = 'unknown'

    tweets_list.append([i['created_at'], i['text'], i['user']['id'], i['user']['name'], i['user']['followers_count'],
                        i['user']['friends_count'], i['place']['full_name'], i['place']['country'],i['lang'], i['retweet_count'], i['favorite_count']])
    # print(tweets_list[-1])





# 11 attris
attri = ['created_at', 'text', 'user_id', 'user_name', 'user_followers_count', 'user_friends_count',
         'place_full_name','place_country', 'lang', 'retweet_count', 'favorite_count']
data = pd.DataFrame(tweets_list, columns=attri)

data.to_csv('tweets_out.csv',index=True)