# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:57:51 2018

@author: Yekta
"""
import csv
from scipy import stats
import numpy as np

for a in range(1,13):
    dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol2/573x60/row/row"+str(a)+".csv")))
    temp=np.asarray(dataFromCSV)
    for n in range(1,562):
        temp1=temp[n,1:]
        temp1 = temp1.astype(np.float)
        temp1=stats.zscore(temp1)
        temp[n,1:]=temp1[:]     
    with open("C:/Users/Yekta/Desktop/stajvol2/573x60/t_score/tsco"+str(a)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(temp)  