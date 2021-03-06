# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:28:51 2021

@author: heidi
"""
import math as math

## Task 1: Multiple of 3 and 5
def multiples_sum(n=10,a=3,b=5):
    L=[i for i in range(1,n) if (i%a==0 or i%b==0)]
    return sum(L)

def fibonacci_sum(B=10,value=None):
    prev=[1,2]
    if value=="Even":
        L=prev[1]
        while sum(prev)<B:
            prev=[prev[1],sum(prev)]
            if (prev[1])%2==0:
                L=L+prev[1]
    elif value=="Odd":
        L=prev[0]
        while sum(prev)<B:
            prev=[prev[1],sum(prev)]
            if (prev[1])%2==1:
                L=L+prev[1]
    else:
        L=sum(prev)
        while sum(prev)<B:
            prev=[prev[1],sum(prev)]
            L=L+prev[1]
    return L

def primefactor_max(n=13195):
    L=[]
    j=2
    while(j<=n):
        if(n%j==0):
            L.append(j)
        while(n%j==0):
            n=n/j
        j+=1
    return max(L)

def palindrome_prod_max(n=2):
    pal=0
    L=0
    for i in range(10**n-1,10**(n-1)-1,-1):
        for j in range(10**n-1,i-1,-1):
            pal=i*j
            if str(pal)[:round(len(str(pal))/2)]==str(pal)[round(len(str(pal))/2):][::-1]:
                if pal > L:
                    L=pal
    return L
