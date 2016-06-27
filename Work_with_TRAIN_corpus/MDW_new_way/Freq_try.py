# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:23:58 2016

@author: tutela
"""
'''Создание таблицы слов саспен и не саспенс с указанием частотности 
употребления из словаря Ляшевской'''
import csv

my_words = {}
words_freq = {}

with open('made_MDW_sus_vs_nonsus.csv', 'r', encoding = 'utf-8') as file:
    inputfile = csv.reader(file, delimiter = ';')
    for row in inputfile:
        word = row[0]
        my_words[word] = row[1], row[2]
                
with open('freqrnc2011.csv', 'r', encoding = 'utf-8') as f:
    inputf = csv.reader(f, delimiter = '\t')
    for row in inputf:
        key = row[0]
        words_freq[key]= row[2]
        
header = 'word;freq_sus;freq_nonsus;\n'
for word in my_words:
    if word in words_freq:
        MDW = my_words[word]
        if float(MDW[0]) > float(MDW[1]):
            header += word + ';' + words_freq[word] + ';;\n'
        else:
            header += word + ';;' + words_freq[word] + ';\n'
    else:
        header += word + ';;;\n'
with open('freq_table.csv', 'w', encoding = 'utf-8') as ff:           
    ff.write(header)
    
print('Done')