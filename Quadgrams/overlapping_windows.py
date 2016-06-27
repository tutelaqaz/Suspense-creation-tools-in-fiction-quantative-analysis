'''Создание списка квадграмм для саспенса, не саспенса и "других"'''

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
with open('Extracts.csv','r',encoding = 'utf-8') as f:
    for row in csv.reader(f, delimiter = ';'):
        if float(row[1]) > 8.5:
            wordsinline = row[0].split()
            for word in wordsinline:
                m = re.search('([А-я]+)(\\W+|\\W)', word)
                if m != None:
                    word = word.replace(str(m.group(2)), '')
                    words.append(word)
                if m == None:
                    words.append(word)
            replacing(words)
            quadgram_finder = list(ngrams(words, 4))
            with open('Suspense_quadgrams.txt', 'w', encoding = 'utf-8') as f:
                for quadgram in quadgram_finder:
                    f.write(str(quadgram)+ '\n')
        elif float(row[1]) < 5:
            wordsinline2 = row[0].split()
            for word in wordsinline2:
                m = re.search('([А-я]+)(\\W+|\\W)', word)
                if m != None:
                    word = word.replace(str(m.group(2)), '')
                    words2.append(word)
                if m == None:
                    words2.append(word)
            replacing(words2)
            quadgram_finder2 = list(ngrams(words2, 4))
            with open('NonSuspense_quadgrams.txt', 'w', encoding = 'utf-8') as f:
                for quadgram in quadgram_finder2:
                    f.write(str(quadgram)+ '\n')
        else:
            wordsinline3 = row[0].split()
            for word in wordsinline3:
                m = re.search('([А-я]+)(\\W+|\\W)', word)
                if m != None:
                    word = word.replace(str(m.group(2)), '')
                    words3.append(word)
                if m == None:
                    words3.append(word)
            replacing(words3)
            quadgram_finder3 = list(ngrams(words3, 4))
            with open('Other_quadgrams.txt', 'w', encoding = 'utf-8') as f:
                for quadgram in quadgram_finder3:
                    f.write(str(quadgram)+ '\n')
        
print("Done")
