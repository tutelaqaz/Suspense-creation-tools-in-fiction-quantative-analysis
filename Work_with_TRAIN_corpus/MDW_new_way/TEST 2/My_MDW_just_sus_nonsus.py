# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:02:19 2016

@author: tutela
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 26 22:29:09 2016

@author: tutela
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:04:06 2016

@author: tutela
"""
''' Процесс выделения MDW с множителем 4'''
import os

import nltk

import numpy as np
import csv


from sklearn.feature_extraction.text import CountVectorizer

filenames = ['made_Suspense.txt', 'made_NonSuspense.txt', 'made_Other.txt']

raw_texts = []
stops = [] 
'''
with open('stop_words.csv', 'r', encoding = 'utf-8') as f:
    stop_file = csv.reader(f, delimiter = '\t')
    for row in stop_file:
        word = row[0].strip(' ')
        stops.append(word)
'''    
for file in filenames:
   with open(file, encoding = 'utf-8') as f:
       text = f.read()
       raw_texts.append(text)

vectorizer = CountVectorizer(input='content')

dtm = vectorizer.fit_transform(raw_texts)

vocab = np.array(vectorizer.get_feature_names())

# fit_transform returns a sparse matrix (which uses less memory)
# but we want to work with a normal numpy array.
dtm = dtm.toarray()

# normalize counts to rates per 1000 words
rates = 1000 * dtm / np.sum(dtm, axis=1, keepdims=True)
        
file = open('madewords_table.txt', 'w', encoding = 'utf-8')
words_table = 'words\\files;Suspense;NonSuspense;Other;\n'

for i, word in enumerate(vocab):
    sus = rates[0, i]
    Nonsus = rates[1, i]
    other = rates[2, i]
    words_table += (word + ';' + str(sus) + ';' + str(Nonsus) + ';' + 
                    str(other) + ';' + '\n')
file.write(words_table)
file.close()

# indices so we can refer to the rows for the relevant author
Suspense_indices, Nonsuspense_indices, other_indices = [], [], []

for index, fn in enumerate(filenames):
    if "_Suspense" in fn:
        Suspense_indices.append(index)
    elif "made_Non" in fn:
        Nonsuspense_indices.append(index)
    elif "made_Other" in fn:
        other_indices.append(index) 

# this kind of slicing should be familiar if you've used R or Octave/Matlab
Suspense_rates = rates[Suspense_indices, :]

Nonsuspense_rates = rates[Nonsuspense_indices, :]

other_rates = rates[other_indices, :]

# np.mean(..., axis=0) calculates the column-wise mean
Suspense_rates_avg = np.mean(Suspense_rates, axis=0)

Nonsuspense_rates_avg = np.mean(Nonsuspense_rates, axis=0)

other_rates_avg = np.mean(other_rates, axis=0)

# since zero times any number is zero, this will identify documents where
# any author's average rate is zero
#distinctive_indices = (Suspense_rates_avg * Nonsuspense_rates_avg) == 0
#distinctive1_indices = (Suspense_rates_avg * other_rates_avg) == 0
#distinctive2_indices = (Nonsuspense_rates_avg * other_rates_avg) == 0

# examine words that are unique, ranking by rates
#print(np.count_nonzero(distinctive_indices))
#print(np.count_nonzero(distinctive1_indices))
#print(np.count_nonzero(distinctive2_indices))

#ranking = np.argsort(Suspense_rates_avg[distinctive_indices] + Nonsuspense_rates_avg[distinctive_indices])[::-1]  # from highest to lowest; [::-1] reverses order.

#smth = vocab[distinctive_indices][ranking]

file = open('made_MDW_sus_vs_nonsus_4.txt', 'w', encoding = 'utf-8')
MDW_table = 'words\\files;Suspense;NonSuspense;\n'

for i, word in enumerate(vocab):
    sus = rates[0, i]
    Nonsus = rates[1, i]
    other = rates[2, i]
    if sus != 0 or Nonsus != 0:
        if sus > 5*Nonsus and sus > 5*other:
            MDW_table += (word + ';' + str(sus) + '; ;\n')
        if Nonsus > 5*sus and Nonsus > 5*other:
            MDW_table += (word + '; ;' + str(Nonsus) + ';\n')
        
            
file.write(MDW_table)
file.close()

print('Done')
