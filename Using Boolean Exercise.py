# -*- coding: utf-8 -*-
"""
Created on Thu May 30 22:00:30 2019

@author: Lawrence
"""
shipping=True
amountPurchase=int(input("Enter your deposit amount:"))
if amountPurchase <50:
    shipping=False
    print("Please add an extra 10$")
print("Shipping is free 0.00$")    

    