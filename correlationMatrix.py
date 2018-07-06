# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 14:45:45 2018

@author: Yekta
"""

import numpy as np
import csv

for k in range(1,13):
    dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/staj/secondway/"+str(k)+"normal.csv")))
    
    matfloat = [[0 for x in range(52)] for y in range(573)]
    
    for o in range(1,574):
        for s in range(1,53):
            try:
                matfloat[o-1][s-1]=float(dataFromCSV[o][s])
            except ValueError:
                matfloat[o-1][s-1]=0
                
    mat=np.corrcoef(matfloat)
    mat=mat.tolist()
    matfin = [[0 for x in range(574)] for y in range(574)]
    matfin[0][0]='Properties'
    
    for r in range(1,574):
        matfin[0][r]=dataFromCSV[r][0]
        matfin[r][0]=dataFromCSV[r][0]
        matfin[r][1:]=mat[r-1][:]
        
    
    with open("C:/Users/Yekta/Desktop/staj/secondway/corrMatrixes"+str(k)+".csv", 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerows(matfin)
            