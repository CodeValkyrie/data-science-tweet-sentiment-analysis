import pandas as pd
tweets = pd.read_json('data.json')

#reading only few for testing
tweets = tweets[:5].copy()

import re

# A function that extracts the hyperlinks from the tweet's content.
def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

# A function that checks whether a word is included in the tweet's content
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

#tweets[tweets['link'] != ''].index
for i in tweets[tweets['link'] != ''].index:
    tweets['text'].loc[i] = re.sub(r"http\S+", "", tweets['text'].loc[i])

del tweets['link']


