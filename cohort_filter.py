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
    '''
    This function to iterates on the datasets then, 
    produce the output with cohort_filter function.
    '''
    for cohort in cohorts:
        target = cohort + '.txt'
        output = cohort + '_90.txt'        
        cohort_filter(target, output)
    return 'Done!'

def cohort_filter(target, output):
    '''
    This function is for filter the dataset per gene or per each line (gene).
    '''
    # It opens the target file and open the output to prepare it
    f = open(target, "rb")
    output = output
    o = open(output, "wb")
    
    # Read first the header of the target file then write it at the output file.
    head = f.readline()
    o.write(head)
    
    # Checking each gene or each line 
    for line in f:
        # Strip first the enter so it will not annoy you later, then split by tab.
        row = line.rstrip('\n').split('\t')
        
        # Counter: for calculating percentage to be filtered.
        counter = 0
        '''  
        Iteration on the line. It try to change the value to float type, then counts it to counter variable
        if it fails, it goes to except flow, then if it encounters ValueError, due to "NAN", "Null", "",
        it will be treated as zero, so it adds to the counter variable.
        '''
        for i in row:
            if row.index(i) == 0:
                pass
            else:
                try:
                    if float(i) == 0:
                        counter+=1
                except (ValueError):
                    counter+= 1
        
        # Calculating the percentage.
        percentage = counter/float((len(row)-1)) * 100
        # Only if the percentage of zero values of each gene below than 10.
        # Then it will write down the line to the output file.
        if percentage < 10:
            o.write('\t'.join(row[0:]) + '\n')
        
    print target, "Done!"
    
    f.close()
    o.close()
    return 'Done!'

#This print of iter_cohort function will run on each dataset on the cohorts.
#print iter_cohort(cohorts) 

'''
All the functions below is for checking purposes.
You can neglect all the functions below.
'''            
def iter_null_finder(cohorts):
    '''
    This will iterate on all the cohorts with the null_finder function.
    '''
    for cohort in cohorts:
        target = cohort + '.txt'       
        null_finder(target)
    return 'Done!'

def null_finder(target):
    '''
    This function will check and count all the ValueError available.
    '''
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
    '''
    This function was made to handle the ITOM dataset, 
    because in the dataset, it has 'nan' value. It is hard to handle 'nan' value in Python
    That is why I chose to replace the 'nan' into 0.0000 to make it easier.
    '''
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

