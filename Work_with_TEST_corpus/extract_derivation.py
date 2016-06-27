# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:35:59 2016

@author: tutela
"""

from nltk.stem.snowball import RussianStemmer
from nltk.util import ngrams
import csv
import re
def replacing(words):
    for word in words:
        if word == '-' or word =='--' or word =='—':
            words.remove(word)
    return words
books = ['Bad_night.csv', 'Cave.csv', 'I_killed.csv', 'Mamai.csv']
extracts = []
extracts2 = []
extracts3 = []
for book in books:
    with open(book,'r',encoding = 'utf-8') as f:
        for row in csv.reader(f, delimiter = ';'):
            if float(row[1]) > 8.5:
                extracts.append(row[0])
            elif float(row[1]) < 5:
                extracts2.append(row[0])
            
            else:
                extracts3.append(row[0])
            

with open('Suspense_extracts_test.txt', 'w', encoding = 'utf-8') as file:
    for extract in extracts:
        file.write(extract + '\n')
with open('NonSuspense_extracts_test.txt', 'w', encoding = 'utf-8') as file:
    for extract in extracts2:
        file.write(extract + '\n')
with open('Other_extracts_test.txt', 'w', encoding = 'utf-8') as file:
    for extract in extracts3:
        file.write(extract + '\n')

    
print("Done")