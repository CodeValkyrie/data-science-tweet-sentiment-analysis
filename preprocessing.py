import numpy as np
import pandas as pd
from spellchecker import SpellChecker
import re

# Initializes the spell checker and lammatizer.
check = SpellChecker()

# Reads in the data.
data = pd.read_json('data.json')

#reading only few for testing
data = data[:5].copy()

########################### FUNCTIONS ###################################
def correct_text(text):
# text needs to be a list of clean word tokens without other characters.
    misspelled = check.unknown(text)
    for word in misspelled:
        text[text.index(word)] = check.correction(word)
    return text

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

######################### CLEANING ###########################################
data['link'] = data['text'].apply(lambda tweet: extract_link(tweet))

#tweets[tweets['link'] != ''].index
for i in data[data['link'] != ''].index:
    data['text'].loc[i] = re.sub(r"http\S+", "", data['text'].loc[i])

del data['link']

# for row in dataframe:
#     text_in_row = cleaned text1
#     text_in_row = cleaned_text2

data = data.replace("", np.nan).dropna()


