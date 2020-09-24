import pandas as pd
import numpy as np

################################################ FUNCTIONS ###################################################
def get_n_tweets(data):
    return len(data.index)

def get_n_per_col_value(data, column):
    return data[column].value_counts()

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
# print("From this {} tweet states are known and {} tweets are from unknown states.".format(n_tweet_states, n_unknown))