import pandas as pd
import numpy as np
from descriptive_statistics import get_n_per_col_value

data = pd.read_csv("clean_twitter_data.csv", index_col=0)

# Checking proportion of candidate tweets in original data frame.
print("Clinton tweets: ", len(data[data['candidate'] == 'clinton'].index))
print("Trump tweets: ", len(data[data['candidate'] == 'trump'].index))

# Checking the distribution of tweets over the states in the original data frame.
distribution = get_n_per_col_value(data, 'states')
normalised_dis_original = distribution / distribution.sum()
print(normalised_dis_original)

sample = data.sample(50000, random_state=1)

print(sample)
print(len(sample.index))

# Checking proportion of candidate tweets in sample data frame.
print("Clinton tweets: ", len(sample[sample['candidate'] == 'clinton'].index))
print("Trump tweets: ", len(sample[sample['candidate'] == 'trump'].index))

# Checking the distribution of tweets over the states in the original data frame.
distribution = get_n_per_col_value(data, 'states')
normalised_dis_sample = distribution / distribution.sum()
print(normalised_dis_sample)

# Comparing the distribution ranks of the states between the original and sample data frames.
print("original: ", normalised_dis_original.index)
print("sample: ", normalised_dis_sample.index)

sample.to_csv("cleaned_twitter_data_50000_sample.csv")
