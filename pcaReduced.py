# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 09:42:18 2018

@author: Yekta
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:21:01 2018

@author: Yekta
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA

tt=[]
for m in range(1,13):
    dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/573x96/rowReduced/reducedRow"+str(m)+".csv")))
    array=np.asarray(dataFromCSV)
    
    temp = [[0 for x in range(np.size(array,1)-1)] for y in range(np.size(array,0)-1)]
    
    for x in range(1,np.size(array,1)):
        for y in range(1,np.size(array,0)):
            try:
                temp[y-1][x-1]=float(dataFromCSV[y][x])
            except ValueError:
                temp[y-1][x-1]=0
    
    dataset = pd.read_csv("C:/Users/Yekta/Desktop/stajvol3/573x96/rowReduced/reducedRow"+str(m)+".csv")
    data = pd.DataFrame(columns=[array[0,1:]], index=[dataset.iloc[:,0].values])
    for x in range(0,np.size(array,0)-1):
        for y in range(0,np.size(array,1)-1):
            data.iloc[x,y] = temp[x][y]
    
    scaled=preprocessing.scale(data.T)
    
    pca = PCA()
    pca.fit(scaled)
    pca_data=pca.transform(scaled)
    
    per_var=np.round(pca.explained_variance_ratio_*100, decimals=1)
    t=0
    r=0
    for x in (per_var):
        if t < 99:
            t=per_var[r]+t
            r=r+1
        else:
            break
    d=0
    ff=[]
    labels = ['PC' +str(x) for x in range(1, r+1)]
    
    for j in labels:
        ff.append(per_var[d])
        d=d+1
    tt.append(ff)
    
    fin = [[0 for x in range(len(labels)+1)] for y in range(np.size(array,0))]
    fin[0][0]='Properties'
    for t in range (0,len(labels)):
        loading_scores = pd.Series(pca.components_[t], index=[dataset.iloc[:,0].values])
        for z in range(0,len(loading_scores)):
            fin[z+1][t+1]=loading_scores.iloc[z]
        if t == len(labels)-1:
            for z in range(0,len(loading_scores)):
                fin[z+1][0]=dataFromCSV[z+1][0]
    for t in range (0,len(labels)):
        fin[0][t+1]=labels[t]
    with open("C:/Users/Yekta/Desktop/stajvol3/573x96/pcaReducedData/pcaReducedData"+str(m)+".csv", 'w', newline='') as myfile:
                    wr = csv.writer(myfile)
                    wr.writerows(pca_data)
    with open("C:/Users/Yekta/Desktop/stajvol3/573x96/pcaReduced/pcaReduced"+str(m)+".csv", 'w', newline='') as myfile:
                    wr = csv.writer(myfile)
                    wr.writerows(fin)
with open("C:/Users/Yekta/Desktop/stajvol3/573x96/pcaReducedRatios/pcaReducedRatios.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(tt)