# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:28:37 2016

@author: Tutelaqaz
"""
''' Обработанные слова добавляются в таблицу с частотностью в нашем корпусе '''
import os

import nltk

import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

filenames = ['made_Suspense.txt', 'made_NonSuspense.txt', 'made_Other.txt']

raw_texts = []

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
        
        
file = open('madewords_table2.txt', 'w', encoding = 'utf-8')
words_table = 'words\\files;Suspense;NonSuspense;Other;\n'
f = open('made_other_table.txt', 'w', encoding = 'utf-8')
other_table ='words\\file;Other;\n'

for i, word in enumerate(vocab):
    sus = rates[0, i]
    Nonsus = rates[1, i]
    other = rates[2, i]
    if sus == 0 and Nonsus == 0:
        other_table += (word + ';'  + str(other) + ';' + '\n')
    else:
        words_table += (word + ';' + str(sus) + ';' + str(Nonsus) + ';' + 
                        str(other) + ';' + '\n')
file.write(words_table)
f.write(other_table)
f.close()
file.close()


print('Done')
