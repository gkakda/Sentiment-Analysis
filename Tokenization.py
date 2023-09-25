# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:09:34 2019

@author: RASIK
"""
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import csv as cs
dataSet=[]
token=[]
text=""
with open("Processed.csv","r") as csvFile:
        fileReader=cs.reader(csvFile)
        for row in fileReader:
            if(row!=[]):
                dataSet.append(row)
for row in dataSet:
    for i in range(len(row)):
        text=row[i]
        token.append(word_tokenize(text))
        cs.register_dialect('myDialect', delimiter='/')
        myFile = open('Token.csv', 'w')  
        with myFile:  
            writer = cs.writer(myFile)
            writer.writerows(token)
       