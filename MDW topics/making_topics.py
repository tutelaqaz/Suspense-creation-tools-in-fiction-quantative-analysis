# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:59:18 2016

@author: tutela
"""

#Подсчет результатов после анализа существительных
import csv
sus = {'предмет': [], 'действие': [], 'описание':[], 'профессия': [], 'место':[],
       'абстрактный':[], 'имя':[], 'направление':[], 'восклицание':[], 'стоп':[]}
nonsus = {'предмет': [], 'действие': [], 'описание':[], 'профессия': [], 'место':[],
       'абстрактный':[], 'имя':[], 'направление':[], 'восклицание':[], 'стоп':[]}
with open('made_MDW_with_topic.csv', 'r', encoding= 'utf-8') as file:
    inputfile = csv.reader(file, delimiter = ';')
    for row in inputfile:
        if row[1] != '':
            topic = row[3]
            if topic in sus:
                sus[topic].append(row[0])
        if row[2] != '':
            if str(row[3]) in sus:
                topic = row[3]
                nonsus[topic].append(row[0])
                
table = ''               
with open('MDW_suspense_topics.csv', 'w', encoding = 'utf-8') as file:
    for topic in sus:
        table += str(topic) + ';'
        for word in sus[topic]:
            table += str(word) + ';'
        num = len(sus[topic])
        table += str(num) + ';\n'
    file.write(table)
table = ''
with open('MDW_nonsuspense_topics.csv', 'w', encoding = 'utf-8') as file:
    for topic in nonsus:
        table += str(topic) + ';'
        for word in nonsus[topic]:
            table += str(word) + ';'
        num = len(nonsus[topic])
        table += str(num) + ';\n'
    file.write(table)
print('done')
