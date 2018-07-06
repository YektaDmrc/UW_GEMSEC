# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 12:39:07 2018

@author: Yekta
"""

import csv
matrix = [[0 for x in range(627)] for y in range(574)]



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
            
for o in range(1,574):
    summa=0
    for s in range(1,625):
        summa=summa+matrix[o][s]        
    mean=summa/624
    matrix[o][625]=mean
    summa2=0
    for r in range(1,625):
        summa2=summa2+(matrix[o][r]-mean)**2
    summa2=summa2/624
    deviat=summa2**1/2
    matrix[o][626]=deviat
    
#with open("C:/Users/Yekta/Desktop/staj/secondway/bigboi1.csv", 'w', newline='') as myfile:
#        wr = csv.writer(myfile)
#        wr.writerows(matrix)    

normalmatrix = [[0 for x in range(627)] for y in range(574)]
for o in range(1,574):
    normalmatrix[o][0]=dataFromCSV[o][0]
    normalmatrix[o][625:627]=matrix[o][625:627]
    for s in range(1,625):
        normalmatrix[o][s]=(matrix[o][s]-matrix[o][625])/matrix[o][626]
        if o == 573:
            normalmatrix[0][s]=matrix[0][s]
            
#with open("C:/Users/Yekta/Desktop/staj/secondway/bigboi2.csv", 'w', newline='') as myfile:
#        wr = csv.writer(myfile)
#        wr.writerows(normalmatrix)
    
for z in range(1,13):
    matrixfin = [[0 for x in range(53)] for y in range(574)]
    for i in range(1,53):
        for s in range(0,574):
            matrixfin[s][i]=normalmatrix[s][i+(z-1)*52]
            matrixfin[s][0]=normalmatrix[s][0]
    with open("C:/Users/Yekta/Desktop/staj/secondway/"+str(z)+"normal.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(matrixfin)
            

        
