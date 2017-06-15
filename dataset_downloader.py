# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 18:35:42 2017

@author: Linggih Saputro
"""
#from selenium import webdriver
import urllib
#download the chromedriver first if there isn't any in your dir.
#The path must include the chromedriver program itself
#path_to_chromedriver = 'C:/Users/Linggih Saputro/Documents/gsoc/chromedriver'
#browser = webdriver.Chrome(executable_path = path_to_chromedriver)


cohorts = ['LAML', 'ACC', 'CHOL', 'BLCA', 'CESC', 'COADREAD', 'COAD', 'UCEC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'DLBC', 'LIHC', 'LGG', 'GBMLGG', 'LUAD', 'LUNG', 'LUSC', 'SKCM', 'MESO', 'UVM', 'OV', 'PANCAN', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'STAD', 'TGCT', 'THYM', 'THCA', 'UCS']
failed = [] # 'FPPP', 'PANCAN12'

def dataset_urllib(cohorts):
    for cohort in cohorts:
        url = 'https://tcga.xenahubs.net/download/TCGA.' + cohort + '.sampleMap/HiSeqV2'
        name = cohort + '.txt'
        try:
            testfile = urllib.URLopener()
            testfile.retrieve(url, name)
        except:
            print cohort
            failed.append(cohort)
            pass
    print failed
    
dataset_urllib(cohorts)
        
    