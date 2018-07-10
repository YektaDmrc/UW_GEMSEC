# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:29:32 2018

@author: Yekta
"""
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


import openpyxl
import csv
dataFromCSV = list(csv.reader(open("C:/Users/Yekta/Desktop/staj/targetandstructural.csv")))

book = openpyxl.load_workbook("C:/Users/Yekta/Desktop/staj/CaCO3sequences.xlsx")

sheet = book.active

for m in range(1,574):
    matrix = [[0 for x in range(13)] for y in range(53)]
    matrix[0][0]='Clone'
    for n in range(1,13):
        matrix[0][n]=n
    
    for a in range(1,53):
        s=sheet['B'+str(a+1)]
        t=sheet['C'+str(a+1)]
        matrix[a][0]=s.value
        for z in range(0,12):
            num=lettertonum(t.value[z])
            matrix[a][z+1]=dataFromCSV[m][num]
            
    with open("C:/Users/Yekta/Desktop/staj/52x12Matrixes(Third Approach)/RowTables/Row"+str(m)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(matrix)

