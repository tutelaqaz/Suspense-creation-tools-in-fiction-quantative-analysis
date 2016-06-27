# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:13:13 2016

@author: tutela
"""
'''Создание словаря с поз квадграмм '''
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
words3 = []
words_pos = {}
my_words_pos = []
my_words_pos2 = []
my_words_pos3 = []

def freq_list(massives): #Создается словрь квадграм из имеющегося массива 
                            #массивов поз квадграм
    freqs= {}
    for massive in massives:
        if tuple(massive) in freqs:
            freqs[tuple(massive)] += 1
        else:
            freqs[tuple(massive)] = 1
    return freqs

with open('freqrnc2011.csv', 'r', encoding = 'utf-8') as f: #создание словаря word-pos
    inputf = csv.reader(f, delimiter = '\t')
    for row in inputf:
        key = row[0]
        words_pos[key]= row[1]
'''
with open('made_Suspense.txt','r',encoding = 'utf-8') as f:#создание массива массивов quad_pos
    for line in f:
        wordsinline = line.split()
        for word in wordsinline:
            word = word.strip('.,:;?!«\»\'\"')
            words.append(word)
    replacing(words)
    quadgram_finder = list(ngrams(words, 4))
for tuples in quadgram_finder:
    mass = []
    for word in tuples:
       if word in words_pos:
           mass.append(words_pos[word])
       else:
           print(word)
           normal = input('POS')
           mass.append(normal)
    my_words_pos.append(mass)


with open('made_Sus_pos_quadgrams.txt', 'w', encoding = 'utf-8') as file:#запись массива массивов quad_pos
    for mass in my_words_pos:
        file.write(str(mass))
        file.write('\n')

with open('made_Suspense_quadgrams.txt', 'w', encoding = 'utf-8') as f:#создание массива массивов quads
    for quadgram in quadgram_finder:
        f.write(str(quadgram)+ '\n')
'''  
with open('made_NonSuspense.txt','r',encoding = 'utf-8') as f: #создание массива массивов quad_pos
    for line2 in f:
        wordsinline2 = line2.split()
        for word in wordsinline2:
            word = word.strip('.,:;?!«\»\'\"')
            words2.append(word)
    replacing(words2)
    quadgram_finder2 = list(ngrams(words2, 4))
for tuples in quadgram_finder2:
    mass2 = []
    for word in tuples:
       if word in words_pos:
           mass2.append(words_pos[word])
       else:
           print(word)
           normal = input('POS')
           mass2.append(normal)
    my_words_pos2.append(mass2)

'''
with open('made_NonSus_pos_quadgrams.txt', 'w', encoding = 'utf-8') as file:
    for mass in my_words_pos2:
        file.write(str(mass))
        file.write('\n')
    
with open('made_NonSuspense_quadgrams.txt', 'w', encoding = 'utf-8') as f:
    for quadgram in quadgram_finder2:
        f.write(str(quadgram)+ '\n')

with open('made_Other.txt', 'r', encoding = 'utf-8') as f: #создание массива массивов quad_pos
    for line3 in f:
        wordsinline3 = line3.split()
        for word in wordsinline3:
            word = word.strip('.,?!\'\"')
            words3.append(word)
    replacing(words3)
    quadgram_finder3 = list(ngrams(words3, 4))
for tuples in quadgram_finder3:
    mass3 = []
    for word in tuples:
       if word in words_pos:
           mass3.append(words_pos[word])
       else:
           print('word')
           normal = input('POS')
           mass.append(normal)
    my_words_pos3.append(mass3)


with open('made_Other_pos_quadgrams.txt', 'w', encoding = 'utf-8') as file:
    for mass in my_words_pos3:
        file.write(str(mass))
        file.write('\n')    
with open('made_Other_quadgrams.txt', 'w', encoding = 'utf-8') as f:
    for quadgram in quadgram_finder3:
        f.write(str(quadgram)+ '\n')      

freq1 = freq_list(my_words_pos)
'''
freq2 = freq_list(my_words_pos2)
'''
freq3 = freq_list(my_words_pos3)'''

with open('list_of_made_posNONSus_quadgrams.csv', 'w', encoding ='utf-8') as file:
    for mass in freq2:
        file.write(str(mass) + ';' + str(freq2[mass]) + ';\n')

print("Done")