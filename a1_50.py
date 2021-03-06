# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:28:51 2021

@author: heidi
"""

## Task 1: Multiple of 3 and 5
def multiples_sum(n=10,a=3,b=5):
    L=[i for i in range(1,n) if (i%a==0 or i%b==0)]
    return sum(L)

def fibonacci_sum_even(B=10):
    prev=[1,2]
    L=prev[1]
    while sum(prev)<B:
        prev=[prev[1],sum(prev)]
        if (prev[1])%2==0:
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


def smallest_multiple(n=10):
    div={}
    for i in range(n+1):
        p=i
        j=2
        while j<=p:
            div_num=0
            while(p%j==0):
                p=p/j
                div_num+=1
            if i%j==0 and (j not in div or j in div and div_num>div[j]) and div_num!=0:
                div[j]=div_num
            j+=1
    val=1
    for k in div.items():
        val=val*k[0]**k[1]
    return val