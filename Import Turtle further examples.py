# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:29:25 2019

@author: Lawrence
"""

import turtle
nbrsides=20
for steps in range (nbrsides):
    turtle.forward(100)
    turtle.right(360/nbrsides)
    for steps in range (nbrsides):
        turtle.forward(50)
        turtle.right(360/nbrsides)