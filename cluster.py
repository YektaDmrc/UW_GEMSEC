# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:38:11 2018

@author: Yekta
"""

import csv
import numpy as np
from sklearn.cluster import KMeans
clon = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/MoS2BP Binding Characterization_07-11-17_DY.csv")))
for k in range(1,15):
    fin=[]
    for m in range(1,13):
        dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/573x96/recon/location"+str(m)+"/PCA"+str(k)+".csv")))
        dataFromCSV=np.asarray(dataFromCSV)
        dataFromCSV=dataFromCSV.T
        temp=dataFromCSV[1:,1:]
        temp=temp.astype(np.float)
        
        
        #clusters according to properties
        kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
        y_kmeans = kmeans.fit_predict(temp)
        fin.append(y_kmeans)
        
    fin=np.asarray(fin)
    fin=fin.T
    matrix = [[0 for x in range(13)] for y in range(97)]
    matrix[0][0]="Index"
    for z in range(1,97):
        matrix[z][0]=clon[z+1][11]
    for x in range(1,13):
        matrix[0][x]=x
        for y in range(1,97):
            matrix[y][x]=fin[y-1,x-1]
    matrix=np.asarray(matrix)


    with open("C:/Users/Yekta/Desktop/stajvol3/573x96/cluster/clusteredPCA"+str(k)+".csv", 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerows(matrix)