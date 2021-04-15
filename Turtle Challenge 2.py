# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:42:06 2019

@author: Lawrence
"""

import turtle
nmbrsides=int(input("Enter the number of sides of the fugure:"))
for steps in range (nmbrsides):
    turtle.forward(100)
    turtle.right(360/nmbrsides)
for steps in range (nmbrsides):
    turtle.forward(50)
    turtle.right(360/nmbrsides)
    