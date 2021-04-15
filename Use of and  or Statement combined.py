# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:24:49 2019

@author: Lawrence
"""

country=input("Enter the name of the country:").upper()
pet=input("Enter the name of the pet:").upper()
if country== "CANADA" and \
     (pet== "MOOSE" or pet== "BEAVER"):
         print("Do you play hockey too?")