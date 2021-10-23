# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 07:36:25 2020

@author: TajammulNaeem
"""
                 
            # Armstrong Number

n=input("Enter a number: ")
total_sum=0
for i in n:
    initial_sum=int(i)**3
    total_sum+=initial_sum
print(total_sum)
if int(n)==total_sum:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")  