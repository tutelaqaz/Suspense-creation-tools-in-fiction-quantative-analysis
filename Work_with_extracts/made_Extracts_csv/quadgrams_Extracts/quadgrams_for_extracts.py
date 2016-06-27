# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:52:31 2016

@author: tutela
"""

'''Создание словаря с pos квадграмм '''
from nltk.stem.snowball import RussianStemmer
from nltk.util import ngrams
import csv
import re
def replacing(words):
    for word in words:
        if word == '-' or word =='--' or word =='—':
            words.remove(word)
    return words

stemmer = RussianStemmer(ignore_stopwords=True) # Choose a language
words = []
words2 = []
words_pos = {}
my_words_pos = []
my_words_pos2 = []

def freq_list(massives): #Создается словрь квадграм из имеющегося массива 
                            #массивов поз квадграм
    freqs= {('a', 's', 'v', 's'):0, ('s', 'spro', 'v', 'pr'):0, ('s', 'spro', 'part', 'v'):0, 
       ('s', 'v', 'pr', 's'):0, ('v', 's', 'spro', 'v'):0, ('s', 'v', 's', 's'):0,
       ('v', 's', 'pr', 's'):0, ('v', 'pr', 's', 'conj'):0, ('s', 'pr', 's', 's'):0,
       ('spro', 'v', 'pr', 's'):0, ('pr', 's', 'a', 's'):0, ('v', 's', 's', 'v'):0,
       ('pr', 's', 'v', 's'):0, ('s', 's', 'v', 'spro'):0, ('s', 'conj', 'v', 's'):0,
       ('v', 'spro', 'v', 's'):0, ('v', 's', 'conj', 'v'):0, ('v', 'pr', 's', 's'):0,
       ('s', 'pr', 'a', 's'):0, ('s', 'conj', 'v', 'pr'):0, ('a', 's', 'pr', 's'):0,
       ('s', 'pr', 's', 'v'):0, ('pr', 's', 'pr', 's'):0, ('a', 'conj', 'a', 's'):0,
       ('a', 's', 'a', 's'):0, ('a', 's', 'pr', 'a'):0, ('s', 's', 'pr', 's'):0,
       ('v', 'pr', 'a', 's'):0, ('s', 's', 's', 's'):0, ('s', 'v', 'a', 's'):0,     
       ('pr', 'a', 'a', 's'):0, ('s', 'pr', 's', 'conj'):0, ('a', 's', 'v', 'pr'):0,
       ('s', 's', 'v', 'pr'):0}
    for massive in massives:
        if tuple(massive) in freqs:
            freqs[tuple(massive)] += 1
    return freqs
    
def replacing(words):
    for word in words:
        if word == '-' or word =='--' or word =='—' or word == '':
            words.remove(word)
    return words

with open('freqrnc2011.csv', 'r', encoding = 'utf-8') as f: #создание словаря word-pos
    inputf = csv.reader(f, delimiter = '\t')
    for row in inputf:
        key = row[0]
        words_pos[key]= row[1]

header = (" ;('a', 'conj', 'a', 's');('a', 's', 'a', 's');('a', 's', 'pr', 'a');('a', 's', 'pr', 's');('a', 's', 'v', 'pr');('a', 's', 'v', 's');('pr', 'a', 'a', 's');('pr', 's', 'a', 's');('pr', 's', 'pr', 's');('pr', 's', 'v', 's');('s', 'conj', 'v', 'pr');('s', 'conj', 'v', 's');('s', 'pr', 'a', 's');('s', 'pr', 's', 'conj');('s', 'pr', 's', 's');('s', 'pr', 's', 'v');('s', 's', 'pr', 's');('s', 's', 's', 's');('s', 's', 'v', 'pr');('s', 's', 'v', 'spro');('s', 'spro', 'part', 'v');('s', 'spro', 'v', 'pr');('s', 'v', 'a', 's');('s', 'v', 'pr', 's');('s', 'v', 's', 's');('spro', 'v', 'pr', 's');('v', 'pr', 'a', 's');('v', 'pr', 's', 'conj');('v', 'pr', 's', 's');('v', 's', 'conj', 'v');('v', 's', 'pr', 's');('v', 's', 's', 'v');('v', 's', 'spro', 'v');('v', 'spro', 'v', 's');\n")
x = 0
with open('made_Suspense.csv', 'r', encoding = 'utf-8') as file: #создание массива массивов quad_pos
    inputfile = csv.reader(file, delimiter = ';')
    for row in inputfile:
        new_words = []
        quadgram_finder = []
        my_words_pos = []
        x += 1
        words = row[0].split()
        for word in words:
            word = word.strip('.,.-_--.-*~.:;?!«\»\'\"')
            new_words.append(word)
        new_words = replacing(new_words)
        quadgram_finder = list(ngrams(new_words, 4))
        for tuples in quadgram_finder:
            mass = []
            for word in tuples:
                if word in words_pos:
                    mass.append(words_pos[word])
                else:
                    print(word)
                    normal = input('POS ')
                    mass.append(normal)
            my_words_pos.append(mass)
        freqs = freq_list(my_words_pos)
        for mass in sorted(freqs):
            if mass == ('a', 'conj', 'a', 's'):
                header += 'S' + str(x) + ';' + str(freqs[mass]) + ';'
            elif mass == ('v', 'spro', 'v', 's'):
                header += str(freqs[mass]) + ';\n'
            else:
                header +=str(freqs[mass]) + ';'    

header = (" ;('a', 'conj', 'a', 's');('a', 's', 'a', 's');('a', 's', 'pr', 'a');('a', 's', 'pr', 's');('a', 's', 'v', 'pr');('a', 's', 'v', 's');('pr', 'a', 'a', 's');('pr', 's', 'a', 's');('pr', 's', 'pr', 's');('pr', 's', 'v', 's');('s', 'conj', 'v', 'pr');('s', 'conj', 'v', 's');('s', 'pr', 'a', 's');('s', 'pr', 's', 'conj');('s', 'pr', 's', 's');('s', 'pr', 's', 'v');('s', 's', 'pr', 's');('s', 's', 's', 's');('s', 's', 'v', 'pr');('s', 's', 'v', 'spro');('s', 'spro', 'part', 'v');('s', 'spro', 'v', 'pr');('s', 'v', 'a', 's');('s', 'v', 'pr', 's');('s', 'v', 's', 's');('spro', 'v', 'pr', 's');('v', 'pr', 'a', 's');('v', 'pr', 's', 'conj');('v', 'pr', 's', 's');('v', 's', 'conj', 'v');('v', 's', 'pr', 's');('v', 's', 's', 'v');('v', 's', 'spro', 'v');('v', 'spro', 'v', 's');\n")
x = 0
with open('made_NonSuspense.csv', 'r', encoding = 'utf-8') as file: #создание массива массивов quad_pos
    inputfile = csv.reader(file, delimiter = ';')
    for row in inputfile:
        new_words2 = []
        quadgram_finder2 = []
        my_words_pos2 = []
        x += 1
        words = row[0].split()
        for word in words:
            word = word.strip('.,.-_--.-*~.:;?!«\»\'\"')
            new_words2.append(word)
        new_words2 = replacing(new_words2)
        quadgram_finder2 = list(ngrams(new_words2, 4))
        for tuples in quadgram_finder2:
            mass2 = []
            for word in tuples:
                if word in words_pos:
                    mass2.append(words_pos[word])
                else:
                    print(word)
                    normal = input('POS ')
                    mass2.append(normal)
            my_words_pos2.append(mass2)
        freq2 = freq_list(my_words_pos2)
        for mass in sorted(freq2):
            if mass == ('a', 'conj', 'a', 's'):
                header += 'S' + str(x) + ';' + str(freq2[mass]) + ';'
            elif mass == ('v', 'spro', 'v', 's'):
                header += str(freq2[mass]) + ';\n'
            else:
                header +=str(freq2[mass]) + ';'

with open('made_NonSus_pos_quadgrams.txt', 'w', encoding = 'utf-8') as file:
    for mass in my_words_pos2:
        file.write(str(mass))
        file.write('\n')
    
with open('made_NonSuspense_quadgrams.txt', 'w', encoding = 'utf-8') as f:
    for quadgram in quadgram_finder2:
        f.write(str(quadgram)+ '\n')

      

freq1 = freq_list(my_words_pos)


file = open('list_of_made_pos_Sus_quadgrams.csv', 'w', encoding ='utf-8')
file.write(header)
file.close()

print("Done")
