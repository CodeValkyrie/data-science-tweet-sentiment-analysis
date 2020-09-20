import numpy as np
import pandas as pd
import nltk
import re
from spellchecker import SpellChecker
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import demoji
from bs4 import BeautifulSoup
demoji.download_codes()

# Initializes the spell checker, tokenizer and lammatizer.
check = SpellChecker()
tokenizer = RegexpTokenizer(r'\w+')
lemma = WordNetLemmatizer()

# Create a set of stopwords
stop_words = set(stopwords.words('english'))

# Create a set of punctuation words
# exclude = set(string.punctuation)

# Reads in the data.
data = pd.read_json('data.json')

#reading only few for testing
# data = data[:5].copy()

########################### FUNCTIONS ###################################
def correct_text(text):
# text needs to be a list of clean word tokens without other characters.
    misspelled = check.unknown(text)
    for word in misspelled:
        text[text.index(word)] = check.correction(word)
    return text

def lemmatize_text(text):
    return [lemma.lemmatize(word) for word in text]

# removing URL links (http or www pattern)
def rm_URL_lowcase(record: str) -> str:
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    sub_record = re.sub(regex, '', record)
    return sub_record

# removing hashtags and @
def rm_hashtags(record: str) -> str:
    sub_record = re.sub(r'@|#', '', record)
    return sub_record

# removing punctuation
def rm_punctuation(record: str) -> str:
    s = re.sub(r'[^\w\s]', '', record)
    return s


# removing stopwords - i.e. the, a, an, he\
def rm_stopwords(record: str) -> str:
    words = list(record.split(' '))
    filtered_sentence = ' '.join([w for w in words if not w in stop_words])
    return filtered_sentence

# removeing emoji
def rm_emoji(record: str) -> str:
    plain = demoji.replace(record, " ")
    return plain

# Removing html coding
def rm_html(record: str) -> str:
    soup = BeautifulSoup(record, 'html.parser')
    plain = soup.get_text()
    return plain

######################### CLEANING ###########################################

for i in data.index:
    print(data['text'].loc[i])
    text = data['text'].loc[i]

    # Removing URL links (http pattern).
    text = re.sub(r'https?://[^\s<>"]+|www\.[^\s<>"]+', "", text)

    # !!!! Removing hashtags and @.  using BeautifulSoup (cases like:  &amp - tweet 9)? WENHAO & ROEL
    text = rm_hashtags(text)
    text = rm_stopwords(text)

    # !!!! Replacing or removing emojis - ROEL
    text = demoji.replace(text, " ")

    # Lowercasing.
    text = text.lower()

    # !!!! Removing punctuation. WENHAO
    text = rm_punctuation(text)

    # !!!! Removing stopwords - i.e. the, a, an, he. WENHAO
    text = rm_stopwords(text)

    # ????some negation handling - how to keep the negation meaning????

    # check cases with more than 140 characters - No text has more than 140 chars

    # Tokenization.
    text = tokenizer.tokenize(text)

    # Removing repeating letters (i.e. awesooome to awesome, *)
    text = correct_text(text)

    # lemmatizing the words
    text = lemmatize_text(text)

    data['text'].loc[i] = text


# Removing all the rows that are empty in the text column after cleaning
data = data.replace("", np.nan).replace([], np.nan).dropna()


