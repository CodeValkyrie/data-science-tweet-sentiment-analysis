import json 
from pathlib import Path


count = 0

tweets_data = []
missed = 0

with open("/Users/kuba/Downloads/geotagged_tweets_20160812-0912.jsons", "r") as f:
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
    d['text'] = tweet['text']
    d['followers_count'] = tweet['user']['followers_count']

    tweets_to_stay.append(d)
    

filename = Path('data.json')
filename.touch(exist_ok=True)

with open('data.json','w') as fp:
    json.dump(tweets_to_stay, fp)

