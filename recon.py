# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:38:11 2018

@author: Yekta
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA

for m in range(1,13):
    dataCSV= list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol2/573x60/row_updated/updatedRow"+str(m)+".csv")))
    dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol2/573x60/pca_updated/pcaUpdated"+str(m)+".csv")))
    data = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol2/573x60/pca_updated_data/data"+str(m)+".csv")))
    
    dataFromCSV=np.asarray(dataFromCSV)
    data=np.asarray(data)
    datacons=np.asarray(dataCSV)
    
    data=data.astype(np.float)
    pc=dataFromCSV[1:,1:]
    pc=pc.astype(np.float)
    
    for n in range(0,12):
        for y in range(1,np.size(dataCSV,0)):
            for x in range(1,np.size(dataCSV,1)):
                datacons[y,x]=pc[y-1,n]*data[x-1,n]
        with open("C:/Users/Yekta/Desktop/stajvol2/573x60/recon/"+str(m)+"/PCA"+str(n+1)+".csv", 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerows(datacons)
            
    
    