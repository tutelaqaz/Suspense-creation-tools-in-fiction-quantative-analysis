# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:37:43 2016

@author: tutela
"""
''' Построение сапенс и не саспенс графика с использованием частотного 
словаря Ляшевской'''
import csv
import numpy as np
import matplotlib.pyplot as plt

sus = []
nonsus = []
stops = []
sus_little =[]
nonsus_little = []
x = 0
with open('stop_words.csv', 'r', encoding = 'utf-8') as f:
    stop_file = csv.reader(f, delimiter = '\t')
    for row in stop_file:
        word = row[0].strip(' ')
        stops.append(word)
    
with open('freq_table.csv', 'r', encoding = 'utf-8') as file:
    justfile = csv.reader(file, delimiter = ';')
    for row in justfile:
        if x != 0:
            if row[0] not in stops:
                
                if str(row[1]) != '':
                    sus.append(float(row[1]))
                if str(row[2]) != '':
                    nonsus.append(float(row[2]))
        x += 1
        
sus.sort()
nonsus.sort()

plt.plot(sus, 'r-', nonsus[300:], 'b-')
plt.show()
