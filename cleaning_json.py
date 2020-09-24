import json 
from pathlib import Path
import os
cwd = os.getcwd()

count = 0

tweets_data = []
missed = 0

with open(cwd+"\\geotagged_tweets_20160812-0912.jsons", "r") as f:
    for line in f:
        try:
            tweet = json.loads(line)
            if not tweet['place']['country'] == 'United States':
                continue
            if not tweet['lang'] == 'en':
                continue
            tweets_data.append(tweet)
            count +=1
        except:
            missed+=1
            continue
    
print('missed tweets: ', missed)

tweets_to_stay = []

for tweet in tweets_data:    
    d = {}
    d['created_at'] = tweet['created_at']
    d['text'] = tweet['text']
    d['user_id'] = tweet['user']['id']
    d['user_name'] = tweet['user']['name']
    d['followers_count'] = tweet['user']['followers_count']
    d['friends_count'] = tweet['user']['friends_count']
    d['place_name'] = tweet['place']['full_name']
    d['retweet_count'] = tweet['retweet_count']
    d['favorite_count'] = tweet['favorite_count']

    tweets_to_stay.append(d)
    

filename = Path('data.json')
filename.touch(exist_ok=True)

with open('data.json','w') as fp:
    json.dump(tweets_to_stay, fp)

