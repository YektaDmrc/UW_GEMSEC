# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:38:11 2018

@author: Yekta
"""

import csv
import numpy as np


for m in range(1,13):
    dataFromCSV= list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/573x96/rowReduced/reducedRow"+str(m)+".csv")))
    dataCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/573x96/pca/pca_data/pcaData"+str(m)+".csv")))
    data = list(csv.reader(open("C:/Users/Yekta/Desktop/stajvol3/573x96/pca/pca_loads/pcaLoads"+str(m)+".csv")))
    
    dataFromCSV=np.asarray(dataFromCSV)
    data=np.asarray(data)
    dataCSV=np.asarray(dataCSV)
    
    pca=dataCSV[1:,1:15]
    loads=data[1:15,1:]
    
    
    pca=pca.astype(np.float)
    loads=loads.astype(np.float)
    final=dataFromCSV.T
    
    #Reconstructions from PCAs
    for x in range(0,np.size(pca,1)):
        for y in range(0,np.size(pca,0)):
            for z in range(0,np.size(loads,1)):
                final[y+1,z+1]=pca[y,x]*loads[x,z]
        res=final.T
        with open("C:/Users/Yekta/Desktop/stajvol3/573x96/recon/location"+str(m)+"/PCA"+str(x+1)+".csv", 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerows(res)
            
    
    