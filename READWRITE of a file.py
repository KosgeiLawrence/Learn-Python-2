# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:12:48 2019

@author: Lawrence
"""

fileName='School.csv'
READ = 'r'
WRITE = 'W'
READWRITE = 'w+'
file = open(fileName , mode=READWRITE)
file.write('Welcome to open data site your best site for online content \n')
file.write('Visit www.google.com')
file.close()