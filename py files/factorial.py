# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 07:36:25 2020

@author: TajammulNaeem
"""
            # Factorial
            
n=int(input("Enter a number: "))
if n==1 or n==0:
    print(f"Factorial {n} is 1")
else:
    f=1
    for i in range(1,n+1):
        f=f*i
print(f"Factorial of {n} is {f}.")