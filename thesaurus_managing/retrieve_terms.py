#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: pmchozas
"""


import json


preflist_es=[]
altlist_es=[]
preflist_en=[]
altlist_en=[]




'''

with this script, we extract a raw list of terms in a given language from thesaurus in skos
'''
with open('../data/labourlaw_thesaurus.json') as jsonfile:
    data= json.load(jsonfile)
    for alldata in data:
        for topconcept in alldata['@graph']:
            try:
                for concept in topconcept['http://www.w3.org/2004/02/skos/core#prefLabel']:
                    if concept['@language'] == 'es':
                        preflist_es.append(concept['@value'])
                    if concept['@language'] == 'en':
                        preflist_en.append(concept['@value'])
            except:
                continue
            try:
                for concept in topconcept['http://www.w3.org/2004/02/skos/core#altLabel']:
                    if concept['@language'] == 'es':
                        altlist_es.append(concept['@value'])
                    if concept['@language'] == 'en':
                        altlist_en.append(concept['@value'])
            except:
                continue
        


print(preflist_en)
print(preflist_es)
print(altlist_en)
print(altlist_es)


with open('../data/llterms_es.txt', 'w') as f:
    for item in preflist_es:
        f.write("%s\n" % item)
    for syn in altlist_es:
        f.write("%s\n" % syn)
        
        
f.close()
