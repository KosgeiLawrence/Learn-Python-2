# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:40:49 2019

@author: Lawrence
"""

#Open my file
schoolName = open('Schools.txt', 'r')
allFilecontent = schoolName.read()
print(allFilecontent)