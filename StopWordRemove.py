# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 19:32:03 2019

@author: RASIK
"""

import csv as cs
#from nltk.corpus import stopwords 
#from nltk.tokenize import word_tokenize
dataSet=[]
final=[]
finalData=[]
temp1=[]

temp2=['?','...','.','``','!','t',"'s",':','s',"'ll","''",'d','|',
      '(',')','#','ABC','ÿ','E',']','[','-',"'em'",'ca',"n't'","'re",';','&','to','be', 'Canadian',
      'I', 'have','life', 'in', 'Cleveland', 'before', 'going', 'New', 'York','we', 'all',
      'a','do','call', 'it','been','entire', 'back', 'story','was', 'supposed', 'an', 'architect', 'ffs',
      'them', 'over','Where', 'Each','gets', 'season','my', 'kids', 'how', 'met', 'their', 'mother', 'on',
      'of', 'your', 'and','They','his', 'apartment', 'The','see','he', 'is', 'about', 'the','This', 'show', 'makes', 'me',
      'can','He','time', 'About','line', 'that','from', 'now','should','How', 'each','BEEN', 'PAYING', 'FOR',
      'years','for','HOW', 'MET', 'YOUR', 'MOTHER','THE', 'PAST', 'YEARS','TO','so','but',
      'i','AND','at','here','with', 'ice', 'cream','Im', 'such','Why','started','am',
      'His','dad','get','thats','don','na','or','her','We', 're', 'And','why','this','book',
      'It','When', 'you','-Robin','`','¯','Mosby//','m','What',"'ve",'CA','+','S','IF', 'FINISH', 'SERIES',
      'MY', 'LIFE', 'WILL', 'BE','him','P.s','its','us','You','Je','our','My','dads',
      'A','Me',"'m",'man','moment', 'where','NEXT', 'WEEK','wo', "n't",'let', 'eat',
      'Book','what','Your','if','did','``','?','th','are','$','/month']

with open('Token.csv',"r") as csvFile:
    fileReader=cs.reader(csvFile)
    for row in fileReader:
        dataSet.append(row)

for row in dataSet:
    if(row!=[]):
        final.append(row)
 

for row in final:
    temp3=[]
    for i in range(len(row)):
        if(row[i] not in temp2):
            temp3.append(row[i])
            
    temp1.append(temp3)    
print(temp1)    
cs.register_dialect('myDialect', delimiter='/')

myFile = open('StopWords.csv', 'w')  
with myFile:
    writer = cs.writer(myFile)
    writer.writerows(temp1)       
        