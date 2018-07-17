# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:15:58 2018

@author: Yekta
"""

import csv
import numpy as np
for m in range(1,13):
    dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/573x96/corr/corr"+str(m)+".csv")))
    array=np.asarray(dataFromCSV)
    
    dataFromCSV2 = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/573x96/row/row"+str(m)+".csv")))
    array2=np.asarray(dataFromCSV2)
    array3=np.asarray(dataFromCSV2)
    
    b=1
    a=1
    
    matrixtest = [[0 for x in range(561)] for y in range(561)]
    t=1
    qq=[]
    
    while(a<=560):
        for x in array[a+1:,a]:
            if(float(x)>0.9):
                qq.append([t+1,a])
            matrixtest[t+1][a]=x
            t=t+1
        a=a+1
        t=a
        
    qq=np.asarray(qq)
    matrixtest=np.asarray(matrixtest)
    qq2=qq[:,0]
    mylist=qq2.tolist()
    used = set()
    unique = [x for x in mylist if x not in used and (used.add(x) or True)]
    unique=sorted(unique, reverse=True)
    
    for x in unique:
        array3 = np.delete(array3, (x), axis=0)
    
    with open("C:/Users/Yekta/Desktop/stajvol3/573x96/rowReduced/reducedRow"+str(m)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(array3)