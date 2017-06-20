# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:15:58 2017

@author: Linggih Saputro
"""
#Itomic is a tab separated value file with \n at the end
itomic = 'itomic_TCGA.txt'
chol = 'CHOL.txt'
dlbc = 'DLBC.txt'

cohorts = ['LAML', 'ACC', 'CHOL', 'BLCA', 'CESC', 'COADREAD', 'COAD', 'UCEC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'DLBC', 'LIHC', 'LGG', 'GBMLGG', 'LUAD', 'LUNG', 'LUSC', 'SKCM', 'MESO', 'UVM', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'STAD', 'TGCT', 'THYM', 'THCA', 'UCS']
pancan = ['PANCAN']
itom = ['ITOM']
def iter_cohort(cohorts):
    for cohort in cohorts:
        target = cohort + '.txt'
        output = cohort + '_90.txt'        
        cohort_filter(target, output)
    return 'Done!'

def cohort_filter(target, output):
    f = open(target, "rb")
    output = output
    o = open(output, "wb")
    
    head = f.readline()
    o.write(head)
    
    for line in f:
        row = line.rstrip('\n').split('\t')
        counter = 0
        for i in row:
            if i == '0.0000' or i == 'NA' or i == 'nan':
                counter+=1
        percentage = counter/float((len(row)-1)) * 100
        if percentage < 10:
            o.write(row[0] + '\t'.join(row[1:]) + '\n')
    f.close()
    o.close()
    return 'Done!'

print iter_cohort(itom)