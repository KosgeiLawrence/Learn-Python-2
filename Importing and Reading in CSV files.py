# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:17:07 2019

@author: Lawrence
"""

import csv
with open('Schools.txt', 'r') as schoolNames:
    allNames = csv.reader(schoolNames)
    print(allNames)
    
    for Name in allNames:
        print(Name)
        for word in Name:
            print(word)
    