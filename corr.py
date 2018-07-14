# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:00:53 2018

@author: Yekta
"""

import csv
import numpy as np

for a in range(1,13):
    dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol2/573x60/t_score/tsco"+str(a)+".csv")))
    dataFromCSV=np.asarray(dataFromCSV)
    matrix=dataFromCSV[1:,1:]
    matrix = matrix.astype(np.float)
    
    fin=np.corrcoef(matrix)
    
    final=np.empty([np.size(fin,0)+1,np.size(fin,0)+1])
    final[1:,1:]=fin[:,:]
    
    for x in range(1,np.size(fin,0)+1):
        final[0,x]=dataFromCSV[x,0]
        final[x,0]=dataFromCSV[x,0]
    
    
    with open("C:/Users/Yekta/Desktop/stajvol2/573x60/corr/tScoCorr"+str(a)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(final)