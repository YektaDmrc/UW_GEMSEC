# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 09:27:22 2018    19541851749  5434781

@author: Yekta
"""
###########################################################
#See the random walk according to seeds
"""
import turtle
from random import seed
from random import randint
#You can change seed here if you delete at all it uses default seed which is obtained from computer clock. It might be more random than giving a seed by hand
#If you use the same seed you will result with the same randomized sets since it is actually deterministic and depends on seed
seed(5434781)

def make_random_walk(step_size, step_number):
    for _ in range(step_number):
        turtle.setheading(18 * randint(1,20))
        turtle.forward(step_size)

if __name__ == "__main__":
    turtle.hideturtle()
    turtle.speed("fastest")
    make_random_walk(10, 12000)
    print("za")
"""
############################################################
from random import randint
from random import seed

import csv
import numpy as np

seq=[]
#Seed is here
seed(5434781)
#You can change generated peptide numbers from here actually we can obtain more than 12.000 if necessary but don't click and open via spider the matrix unless you have good RAM swh
for x in range(0,12000):
    seq.append(randint(1,20))
#I save the sequences we generated to see what they are  
with open("C:/Users/Yekta/Desktop/stajjvol2/gigaMatrix/Seq.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(map(lambda x: [x], seq))

#Change the destionation of the targetandstructural according to your pc. mine has name _added at the end since I added free energy    
dataFromCSV2 = list(csv.reader(open("C:/Users/Yekta/Desktop/stajjvol2/cleaned_targetandstructural_added.csv")))
dataFromCSV2=np.asarray(dataFromCSV2)

#527 properties+1 for rows,12000 columns +1
matrix=np.empty([528,np.size(seq,0)+1])
seq=np.asarray(seq)
seq=seq.reshape(-1,1)


matrix[0,1:]=seq[:,0]

for x in range(1,np.size(seq,0)+1):
    for y in range(1,528):
        matrix[y,x]=float(dataFromCSV2[y,int(matrix[0,x])+3])
for z in range(1,528):
    matrix[z,0]=z
    
with open("C:/Users/Yekta/Desktop/stajjvol2/gigaMatrix/gigaMatrix.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(matrix)

