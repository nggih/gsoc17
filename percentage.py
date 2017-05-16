# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:19:35 2017

@author: Linggih Saputro
"""

import pandas as pd

f = pd.read_csv('HiSeqV2.txt', sep="\t", header = None)

ft = f.transpose()
print ft.head()

'''
Calculating zero expression value
In the BRCA gene by sample matrix, identify the number of genes with >0%, >10%, >25%, >50% samples with zero expression values
'''
# List and number of genes with >0% zero expression values
zero_0 = []

# List and number of genes with >10% zero expression values
zero_10 = []

# List and number of genes with >25% zero expression values
zero_25 = []

# List and number of genes with >50% zero expression values
zero_50 = []


# Using the length of ft:
for k in range(1, len(f)):
    zero_counter = 0
    for i in range(1, len(ft)):
        if float(ft[k][i]) == 0:
            zero_counter += 1
    percentage = (zero_counter/float(len(ft))) * 100
    if percentage > 50:
        zero_50.append(ft[k][0])
    if percentage > 25:
        zero_25.append(ft[k][0])
    if percentage > 10:
        zero_10.append(ft[k][0])
    if percentage > 0:
        zero_0.append(ft[k][0])
        
print '>0%:' + str(len(zero_0))
print '>10%:' + str(len(zero_10))
print '>25%:' + str(len(zero_25))
print '>50%:' + str(len(zero_50))