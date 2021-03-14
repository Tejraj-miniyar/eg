# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:52:06 2020

@author: TEJARAJ
"""

#python program to print prime numbers in given range

lower=int(input("enter lower value"))
upper=int(input("enter upper value"))
for n in range(lower,upper+1):
    if (n>1):
        for i in range(2,n):

            if(n%i==0):
                break
                
        else:
            print(n)

                