# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:18:59 2016

@author: tutela
"""
'''Создание csv файла с количеством частей речи для саспенс и не саспанс'''
import csv

sus ={}
nonsus = {}
sus_with_k = {}
x = 0
y = 0

with open('pos_table.csv', 'r', encoding = 'utf-8') as file:
    inputf = csv.reader(file, delimiter = ';')
    for row in inputf:
        if row[1] != '' and row[1] != 'pos_sus':
            x += 1
            if row[1] in sus:
                sus[row[1]] += 1
            else:
                sus[row[1]] = 1
        if row[2] != '' and row[2] != 'pos_nonsus':
            y += 1
            if row[2] in nonsus:
                nonsus[row[2]] += 1
            else:
                nonsus[row[2]] = 1

z = y/x
for word in sus:
    sus_with_k[word] = int(sus[word]) * z
    sus_with_k[word] = int(sus_with_k[word])
    
header = 'POS;Suspense;Nonsuspense;Suspense_with_k;\n'
with open('pos_histogram.csv', 'w', encoding = 'utf-8') as f:
    for word in sus:
        
        header += (word + ';' + str(sus[word]) + ';' + str(nonsus[word]) + ';' +
                   str(sus_with_k[word]) + ';\n')
        
    f.write(header)   
    
print('Done')
