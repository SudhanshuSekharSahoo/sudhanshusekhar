# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 02:42:33 2020

@author: Milu
"""

import math
nl=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (  lname + " " + fname)

pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

import numpy as np
v=input("Input comma sepatated nos:")
list = v.split(",")
print('list:',list)

word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

string='WE,THE PEOPLE OF INDIA,resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens'
l=string.split('SOCIALIST')
output=l[0]+"!"+"SOCIALIST"+l[1]
print(output)


