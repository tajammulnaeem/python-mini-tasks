# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:47:01 2021

@author: Tajammul
"""

# this code is printing a diomond pattern of asterisks just in two loops.

c=int(input('Enter a integer number: '))
n=c
i=1
while n>=1:
    if n%2==1:
        print(' '*(n//2)+'*'*i+' '*(n//2))
        i+=2
    n=n-1
n=c-2
i=1
while n>=1:
    if n%2==1:
        print(' '*i+'*'*n+' '*i)
        i+=1
    n=n-1