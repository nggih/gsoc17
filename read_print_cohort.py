# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 17:11:01 2017

@author: Linggih Saputro
"""

import pandas as pd
import numpy as np
from multiprocessing import Pool

cohorts = ['LAML', 'ACC', 'CHOL', 'BLCA', 'CESC', 'COADREAD', 'COAD', 'UCEC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'DLBC', 'LIHC', 'LGG', 'GBMLGG', 'LUAD', 'LUNG', 'LUSC', 'SKCM', 'MESO', 'UVM', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'STAD', 'TGCT', 'THYM', 'THCA', 'UCS']
pancan = 'PANCAN'

num_partitions = 10 # number of partititons to split dataframe
num_cores = 4 # number of cores on your machine

def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

def read_pancan(pancan):
    cohort = pancan
    chunksize = 10000
    target = cohort + '.txt'
    name = cohort + '_f.txt'
    output = cohort + '_f10.txt'
    for chunk in pd.read_csv(target, chunksize=chunksize):
        
        f = chunk
        ft = f.transpose()
        
        nz10 = []
        
        # Using the length of ft:
        for k in range(1, len(f)):
            zero_counter = 0
            for i in range(1, len(ft)):
                if float(ft[k][i]) == 0:
                    zero_counter += 1
            percentage = (zero_counter/float(len(ft))) * 100
            if percentage > 10:
                nz10.append(k)
                
        # Make a dataframe out of N - the zero_10.
        df_test = ft.drop(nz10, axis = 1)
        #print df_test
        df_test_t = df_test.transpose()
        #print df_test_t
        
        df_test_t.to_csv(name, sep = '\t', index = False, index_label = False)
        with open(name, 'r') as input:
            input.readline()
            with open('PANCAN_f10.txt' ,'wb') as output:
                for line in input:
                    output.write(line)
chunksize = 10000

for chunk in pd.read_csv('PANCAN.txt', chunksize=chunksize):
    print chunk
    
def read_txt_cohorts(cohorts):
    for cohort in cohorts:
        target = cohort + '.txt'
        name = cohort + '_f.txt'
        output = cohort + '_f10.txt'
        f = pd.read_csv(target, sep="\t", header = None, low_memory=False)
        ft = f.transpose()
        
        '''
        Calculating zero expression value
        In the cancer dataset gene by sample matrix, identify the number of genes with >0%, >10%, >25%, >50% samples with zero expression values
        '''
        # List and number of genes with >10% zero expression values
        zero_10 = []
        nz10 = []
        
        # Using the length of ft:
        for k in range(1, len(f)):
            zero_counter = 0
            for i in range(1, len(ft)):
                if float(ft[k][i]) == 0:
                    zero_counter += 1
            percentage = (zero_counter/float(len(ft))) * 100
            if percentage > 10:
                zero_10.append(ft[k][0])
                nz10.append(k)
                
        # Make a dataframe out of N - the zero_10.
        df_test = ft.drop(nz10, axis = 1)
        #print df_test
        df_test_t = df_test.transpose()
        #print df_test_t
        
        df_test_t.to_csv(name, sep = '\t', index = False, index_label = False)
        with open(name, 'r') as input:
            input.readline()
            with open(output,'wb') as output:
                for line in input:
                    output.write(line)
        
        print cohort + ' Done!'
        
#read_txt_cohorts(cohorts)
        
#read_txt_cohorts(pancan)
#read_pancan(pancan)
