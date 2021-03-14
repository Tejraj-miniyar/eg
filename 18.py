# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:55:52 2020

@author: TEJARAJ
"""

#python program to print fibonacii series

n=int(input("enter how many numbers you want"))
a,b,c,count=0,1,0,0
if(n>=0):
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1
else:
    print("enter a positive number")