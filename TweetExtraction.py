# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:26:59 2019

@author: RASIK
"""

import csv as cs
def readCSVFile(File):
    dataSet=[]
    temp=[[],[' '],[' ø'],[' """???????? ?? ?????? ??????'],['     ?? '],[' -???????????? ??????????????'],['  '],['          '],['        '],['           '],['   '],['      '],['    '],['     '], [' "'],[' ??  '],['                        ']]
    final=[]
    with open(File,"r") as csvFile:
        fileReader=cs.reader(csvFile)
        next(fileReader) #Skip the first row which is row header
        for row in fileReader:
            dataSet.append(row)
    for x in dataSet:
        if x not in temp:
            final.append(x)
    import csv
    csv.register_dialect('myDialect', delimiter='/')

    myFile = open('Processed.csv', 'w')  
    with myFile:  
        writer = csv.writer(myFile)
        writer.writerows(final)    
    #print(final)
readCSVFile('himym17.csv')