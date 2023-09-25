# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:30:26 2019

@author: RASIK
"""

import csv as cs
from textblob import TextBlob
dataSet=[]
final=[]

text=""
with open('StopWords.csv',"r") as csvFile:
    fileReader=cs.reader(csvFile)
    for row in fileReader:
        dataSet.append(row)

for row in dataSet:
    if(row!=[]):
        final.append(row)        

#print(final)  
for row in final:
    text=str(row)
    #print(text)
    analysis = TextBlob(text) 
    if analysis.sentiment.polarity > 0:
        row.append('Positive')
    elif analysis.sentiment.polarity == 0:
        row.append('Neutral')
    else:
        row.append('Negative')

cs.register_dialect('myDialect', delimiter='/')

myFile = open('FinalDataSet.csv', 'w')  
with myFile:
    writer = cs.writer(myFile)
    writer.writerows(final)          
      
