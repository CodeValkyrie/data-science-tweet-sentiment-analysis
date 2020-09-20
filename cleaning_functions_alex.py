import numpy as np
import pandas as pd
from spellchecker import SpellChecker

check = SpellChecker()

def correct_text(text):
# text needs to be a list of clean word tokens without other characters.
    misspelled = check.unknown(text)
    for word in misspelled:
        text[text.index(word)] = check.correction(word)
    return text

data = pd.read_csv("tweets_out.csv", lineterminator='\n')

# ALL THE CLEANING
data = data.replace("", np.nan).dropna()

# AFTER TOKENIZATION the misspellings can be corrected:
