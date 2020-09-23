import pandas as pd
import numpy as np
from gensim import corpora
import gensim
import pickle
import pyLDAvis.gensim
import time

np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)

#display all of the columns
pd.set_option('display.max_columns', None)
#display all of the rows
pd.set_option('display.max_rows', None)
from collections import Counter

############## Cleaned data switch here ################
data = pd.read_csv('cleaned_data.csv')
print(data.shape)
# print(data.iloc[0:10,:])
data = data.iloc[:,1]

text = []
b = 0
start = time.time()
print(start)
interval = 10000
for i in data:
    no_i = i[2:-2]
    cur = list(no_i.split('\', \''))
    text.append(cur)
    # b += 1
    # if b % interval == 0:
    #     print('current progress: '+str(b/data.shape[0]) + ' '+ str(time.time()-start))
#########################################################




dictionary = corpora.Dictionary(text)
corpus = [dictionary.doc2bow(text) for text in text]

pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

##########################################

# NUM_TOPICS = 20
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
# ldamodel.save('model20.gensim')
# topics = ldamodel.print_topics(num_words=4)
# for topic in topics:
#     print(topic)
#
#
# dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
# corpus = pickle.load(open('corpus.pkl', 'rb'))
# lda = gensim.models.ldamodel.LdaModel.load('model20.gensim')
# lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
# pyLDAvis.show(lda_display)
#
# print('end: '+ str(time.time()- start))

##########################################


NUM_TOPICS = 3
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save('model3.gensim')
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)

print('end: '+ str(time.time() - start))

dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
corpus = pickle.load(open('corpus.pkl', 'rb'))
lda = gensim.models.ldamodel.LdaModel.load('model3.gensim')
lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
pyLDAvis.show(lda_display)
