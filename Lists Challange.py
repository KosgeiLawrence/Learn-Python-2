# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:15:20 2019

@author: Lawrence
"""

guests=[]
names="  "
while names.upper()!= "DONE":
    names= input ("Enter the names and when done write done:")
    guests.append(names)
guests.sort()
for guest in guests:
    print(guest.upper())    