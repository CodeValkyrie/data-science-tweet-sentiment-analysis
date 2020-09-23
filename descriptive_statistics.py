import pandas as pd
import numpy as np
from city_state_dict import city_to_state_dict

################################################ FUNCTIONS ###################################################
def get_n_tweets(data):
    return len(data.index)

def get_n_per_col_value(data, column):
    return data[column].value_counts()

def get_state(city):
    if city in city_to_state_dict.keys():
        return city_to_state_dict[city]
    return np.nan

def check_Trump_Clinton(tokenized_text):
    if 'hillaryclinton' in tokenized_text:
        return "clinton"
    elif 'realdonaldtrump' in tokenized_text:
        return "trump"
    elif 'hillary' in tokenized_text:
        return 'clinton'
    elif 'trump' in tokenized_text:
        return "trump"
    else:
        return np.nan

###################################### DESCRIPTIVE STATISTICS ON RAW #########################################
# raw_data = pd.read_csv("tweets_out.csv")
# n_raw_tweets = get_n_tweets(raw_data)
# print("Total number of tweets in original frame: ", n_raw_tweets)
# n_US_tweets = raw_data[raw_data['country'] == 'United States'].index()
# n_foreign_tweets = n_raw_tweets - n_US_tweets
# print("The number of tweets in the US is {} and the number foreign tweets is {}.".format(n_US_tweets, n_foreign_tweets))




###################################### DESCRIPTIVE STATISTICS ON CLEANED #####################################
# data = pd.read_csv("cleaned_data_with_states.csv", index_col='index')
# print(data.columns)
# print(get_n_per_col_value(data, 'states'))
# n_tweets = get_n_tweets(data)
# print("The total number of data points in the data frame is: ", n_tweets)
# n_tweet_states = get_n_per_col_value(data, 'states').sum()
# n_unknown = n_tweets - n_tweet_states
# print("Fron this {} tweet states are known and {} tweets are from unknown states.".format(n_tweet_states, n_unknown))

########################################### ADDING COLUMNS TO DATA ###########################################
data = pd.read_csv("cleaned_data_params.csv", index_col='index')
print(len(data.index))
data['states'] = data['place_full_name'].apply(lambda row: get_state(row))
data['candidate'] = data['text'].apply(lambda row: check_Trump_Clinton(row))

data.to_csv("cleaned_data_with_states_and_candidates.csv")