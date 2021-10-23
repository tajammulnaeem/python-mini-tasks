# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 07:36:25 2020

@author: TajammulNaeem
"""

            # Prime and Not Prime

prime=[]
not_prime=[]
s=int(input('Enter starting number: '))
e=int(input('Enter ending number: '))
while s<=e: 
    r=0
    i = 1
    while i<=s:
        if s%i==0:
            r=r+1
        i=i+1
    if r==2:
        prime.append(s)
    if r!=2:
        not_prime.append(s)
    s=s+1
print('All prime numbers are:',prime)
print('All non_prime numbers are:',not_prime)