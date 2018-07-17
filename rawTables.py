# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 09:10:57 2018

@author: Yekta
"""

# -*- coding: utf-8 -*-

import csv
import numpy as np

def lettertonum(lt):
    if lt == 'A':
        return 3
    elif lt == 'R':
        return 4
    elif lt == 'N':
        return 5
    elif lt == 'D':
        return 6
    elif lt == 'C':
        return 7
    elif lt == 'E':
        return 8
    elif lt == 'Q':
        return 9
    elif lt== 'G':
        return 10
    elif lt == 'H':
        return 11
    elif lt == 'I':
        return 12
    elif lt == 'L':
        return 13
    elif lt == 'K':
        return 14
    elif lt == 'M':
        return 15
    elif lt == 'F':
        return 16
    elif lt == 'P':
        return 17
    elif lt == 'S':
        return 18
    elif lt == 'T':
        return 19
    elif lt == 'W':
        return 20
    elif lt == 'Y':
        return 21
    elif lt == 'V':
        return 22


dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/MoS2BP Binding Characterization_07-11-17_DY.csv")))
dataFromCSV2 = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/targetandstructural.csv")))

skip=[525,524,521,482,481,480,479,478,477,476,475,474,473]

dataFromCSV=np.asarray(dataFromCSV)
dataFromCSV2=np.asarray(dataFromCSV2)

for m in range(1,13):
    matrix=np.empty([np.size(dataFromCSV2,0),np.size(dataFromCSV,0)-1])
    matrix = matrix.astype(np.str)
    matrix[0,0]='Properties'
    matrix[0,1:]=dataFromCSV[2:,m+11]
    for t in range(1,574):
        matrix[t,0]=t
    for x in range(1,97):
        for y in range(1,574):
            matrix[y,x]=dataFromCSV2[y,lettertonum(matrix[0,x])]
    for z in skip:
        matrix=np.delete(matrix,z,0)
    with open("C:/Users/Yekta/Desktop/stajvol3/573x96/row/row"+str(m)+".csv", 'w', newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerows(matrix)
        