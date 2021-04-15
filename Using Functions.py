# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:20:04 2019

@author: Lawrence
"""

def getNames():
    names = [ 'Daniel','Fransis', 'Gabriel' , 'Shem']
    newName = input ('Enter the New Member:')
    names.append(newName)
    print(names)

    return names
getNames()