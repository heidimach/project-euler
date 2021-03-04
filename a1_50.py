# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:28:51 2021

@author: heidi
"""

## Task 1: Multiple of 3 and 5
def multiples_sum(B=10,a=3,b=5):
    L=[i for i in range(1,B) if (i%a==0 or i%b==0)]
    return sum(L)

