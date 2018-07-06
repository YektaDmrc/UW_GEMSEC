# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 00:45:40 2018

@author: Yekta
"""

import csv
matrix = [[0 for x in range(625)] for y in range(574)]


p=1

for a in range(1,13):
    dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/staj/secondway/"+str(a)+".csv")))
    for t in range(0,574):
        matrix[t][p:p+52]=dataFromCSV[t][1:]
    if p == 573:
        for t in range(0,574):
            matrix[t][0]=dataFromCSV[t][0]                    
    p=p+52
    print(p)

for o in range(1,574):
    for s in range(1,625):
        try:
            matrix[o][s]=float(matrix[o][s])
        except ValueError:
            matrix[o][s]=0
            
matrixNormal = [[0 for x in range(625)] for y in range(574)]
matrixNormal[0][:]=matrix[0][:]

for z in range(1,574):
    dum=[]
    dum=matrix[z][1:]
    dum=stats.zscore(dum)
    dum=dum.tolist()
    matrixNormal[z][1:]=dum
    matrixNormal[z][0]=matrix[z][0]

for z in range(1,13):
    matrixfin = [[0 for x in range(53)] for y in range(574)]
    for i in range(1,53):
        for s in range(0,574):
            matrixfin[s][i]=matrixNormal[s][i+(z-1)*52]
            matrixfin[s][0]=matrixNormal[s][0]
    with open("C:/Users/Yekta/Desktop/staj/secondway/"+str(z)+"normalenhanced.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(matrixfin)