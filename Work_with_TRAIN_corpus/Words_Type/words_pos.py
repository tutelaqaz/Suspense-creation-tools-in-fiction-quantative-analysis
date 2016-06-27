# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:58:06 2016

@author: tutela
"""
''' Создание списка слов саспенс и не саспенс и их тип'''

import csv

words_pos = {}
my_words = {}
my_words_pos = {}
freqs = []
with open('freqrnc2011.csv', 'r', encoding = 'utf-8') as f:
    inputf = csv.reader(f, delimiter = '\t')
    for row in inputf:
        key = row[0]
        words_pos[key]= row[1]
      
with open('freq_table.csv', 'r', encoding = 'utf-8') as file:
    inputfile = csv.reader(file, delimiter = ';')
    for row in inputfile:
        word = row[0]
        my_words[word] = row[1], row[2]

header = 'word;pos_sus;pos_nonsus;\n'
for key in my_words:
    freq = my_words[key]
    if key in words_pos:
        if freq[0] != '':
            my_words_pos[key] = [words_pos[key], '']
            header += key + ';'+ words_pos[key] + ';;\n'
        if freq[1] != '':
            my_words_pos[key] = ['', words_pos[key]]
            header += key + ';;'+ words_pos[key] + ';\n'
        
with open('pos_table.csv', 'w', encoding = 'utf-8') as ff:           
    ff.write(header)

print('Done')
