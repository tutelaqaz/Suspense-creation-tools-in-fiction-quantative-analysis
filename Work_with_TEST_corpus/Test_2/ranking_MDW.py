# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:28:22 2016

@author: tutela
"""
import csv

stop_words = []
sus = []
nonsus = []
extracts = ['made_Suspense_test.csv', 'made_NonSuspense_test.csv']
ranks = {}
with open('made_MDW_sus_vs_nonsus_without_stops.csv', 'r', encoding= 'utf-8') as file:
    inputfile = csv.reader(file, delimiter = ';')
    for row in inputfile:
        if row[1] != '':
            sus.append(row[0])
        if row[2] != '':
            nonsus.append(row[0])
            

for doc in extracts:
    with open(doc, 'r', encoding = 'utf-8') as f:
       inputf = csv.reader(f, delimiter = ';')
       for row in inputf:
           ranks[row[0]] = []
           
for abstract in ranks:
    wordsinline = abstract.split()
    sus1 = 0
    nonsus2= 0
    for word in wordsinline:
        if word in sus: 
            sus1 += 1
        if word in nonsus:
            nonsus2 -= 1
    ranks[abstract].append(sus1)
    ranks[abstract].append(nonsus2)
with open('results_table_without_stops.csv', 'w', encoding = 'utf-8') as file:
    for abstract in ranks:
        numer = ranks[abstract]
        file.write(str(abstract) + ';' + str(numer[0]) + ';' + str(numer[1]) +';\n')
        
print('Done')