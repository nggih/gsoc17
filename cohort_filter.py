# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:15:58 2017

@author: Linggih Saputro
"""
cohorts = ['LAML', 'ACC', 'CHOL', 'BLCA', 'CESC', 'COADREAD', 'COAD', 'UCEC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'DLBC', 'LIHC', 'LGG', 'GBMLGG', 'LUAD', 'LUNG', 'LUSC', 'SKCM', 'MESO', 'UVM', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'STAD', 'TGCT', 'THYM', 'THCA', 'UCS']
pancan = ['PANCAN']
large = ['BRCA', 'ITOM']
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
            if row.index(i) == 0:
                pass
            else:
                try:
                    if float(i) == 0:
                        counter+=1
                except (ValueError):
                    counter+= 1
        
        percentage = counter/float((len(row)-1)) * 100
        if percentage < 10:
            o.write('\t'.join(row[0:]) + '\n')
        
    print target, "Done!"
    
    f.close()
    o.close()
    return 'Done!'

#print cohort_filter('ITOM_90f.txt','ITOM_90.txt')
                
def iter_null_finder(cohorts):
    for cohort in cohorts:
        target = cohort + '.txt'       
        null_finder(target)
    return 'Done!'

def null_finder(target):
    f = open(target, "rb")
    head = f.readline()
    statement = {'null': 0}
    for line in f:
        row = line.rstrip('\n').split('\t')
        for i in row:            
            if row.index(i) == 0:
                pass
            else:
                
                try:    
                    float(i)
                except (ValueError):
                    statement['null'] += 1
                    
    print target, "Done!"
    print statement
    
    f.close()
    
    return 'Done!'
   
#print iter_null_finder(['ITOM'])

def nan_replace(target, output):
    f = open(target, "rb")
    output = output
    o = open(output, "wb")
    
    head = f.readline()
    o.write(head)
    
    for line in f:
    #row = line.rstrip('\n').split('\t')
        row = line.replace('nan', '0.0000')
        o.write(row)
        
    print target, "Done!"
    
    f.close()
    o.close()
    return 'Done!'

target = "ITOM_90.txt"
output = "ITOM_90f.txt"

#print nan_replace(target, output)

