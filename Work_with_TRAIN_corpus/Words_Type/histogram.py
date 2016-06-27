# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:42:24 2016

@author: tutela
"""

import csv
import pylab as plt
import plotly as py


sus ={}
nonsus = {}
sus_with_k = {}
x = 0
y = 0
with open('pos_table.csv', 'r', encoding = 'utf-8') as file:
    inputf = csv.reader(file, delimiter = ';')
    for row in inputf:
        if row[1] != '':
            x += 1
            if row[1] in sus:
                sus[row[1]] += 1
            else:
                sus[row[1]] = 1
        if row[2] != '':
            y += 1
            if row[2] in nonsus:
                nonsus[row[2]] += 1
            else:
                nonsus[row[2]] = 1

z = y/x
for word in sus:
    sus_with_k[word] = int(sus[word]) * z
    
    sus_with_k[word] = int(sus_with_k[word])
       
words =[]
words2 = []
fig = plt.figure()
    
for word in sus:
    words.append(sus[word])
    if word in nonsus:
        words2.append(nonsus[word])
    n, bins, patches = plt.hist([words, words2])
    
plot_url = py.offline.plot_mpl(fig, filename='mpl-histogram.html')
    

    
print('Done')

