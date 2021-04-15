# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:30:06 2019

@author: Lawrence
"""

fileName = 'Upper'
WRITE = 'w'
file = open(fileName, mode=WRITE)
file.write('data')
file.close
print('File written succesfuly')