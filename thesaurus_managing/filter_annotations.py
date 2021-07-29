#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:43:56 2021

@author: pmchozas

"""

import re

file=open('../data/annotated/TRAINING_HOHFELD.txt', 'r', encoding='utf-8')
read=file.readlines()

trainfile_terms=[]


for line in read:
    tag1 = re.search('<e1>(.+?)</e1>', line)
    tag2 = re.search('<e2>(.+?)</e2>', line)
    if tag1:
        term = tag1.group(1)
        trainfile_terms.append(term)
    if tag2:
        term = tag2.group(1)
        trainfile_terms.append(term)
        
        
trainfile_terms= list(dict.fromkeys(trainfile_terms))
new=open('../data/filtered_terms.txt', 'w', encoding='utf-8')

for term in trainfile_terms:
    new.write(term+'\n')
    
new.close()
#print(trainfile_terms)
