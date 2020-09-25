import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

################################################ FUNCTIONS ###################################################
def get_n_tweets(data):
    return len(data.index)

def get_n_per_col_value(data, column):
    return data[column].value_counts()

###################################### DESCRIPTIVE STATISTICS ON CLEANED #####################################

# Reads in the data and prints the columns to be analysed.
data = pd.read_csv("cleaned_twitter_data_50000_sample.csv", index_col=0)
print(data.columns)

# Gets the distribution of tweets over the states and plots it.
n_tweets = get_n_tweets(data)
tweet_state_distribution = pd.DataFrame(get_n_per_col_value(data, 'states')/n_tweets)
sns.set_palette(sns.color_palette('Blues_r', 13))
graph = tweet_state_distribution.plot.bar()
plt.legend().remove()
_, labels = plt.xticks()
graph.set_xticklabels(labels, rotation=45, horizontalalignment='right', fontsize='x-small')
plt.title('Tweet Distribution per State')
plt.xlabel("State")
plt.ylabel("Distribution")
plt.tight_layout(2)
plt.show()

clinton_data = data[data['candidate'] == 'clinton']
trump_data = data[data['candidate'] == 'trump']