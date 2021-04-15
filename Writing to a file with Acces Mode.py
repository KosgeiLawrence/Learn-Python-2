# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:48:02 2019

@author: Lawrence
"""

fileName= 'IDT'
write= 'w'
file = open(fileName, mode=write)
file.write('What is the name of your pet?\n')
file.write('what is the name of your friend?')
file.close()