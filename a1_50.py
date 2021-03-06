# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:28:51 2021

@author: heidi
"""
import numpy as np

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

def sum_square_diff(n=10):
    L=sum(range(n+1))**2
    L1=sum([i**2 for i in range(n+1)])
    return L-L1

def nth_prime_number(n=6):
    L=[]
    i=2
    while len(L)!=n:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            L.append(i)
        i+=1
    return L[-1]

def largest_product_in_series(n=4):
    num=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    num_str=str(num)
    p_large=0
    i=0
    while i+n<len(num_str):
        p=num_str[i:i+n]
        p_prd=1
        for j in p:
            p_prd=p_prd*int(j)
        if p_large<p_prd:
            p_large=p_prd
        i+=1
    return

def special_pythagorean_triplet(n=1000):
    B=n
    for b in range(2,B):
        for a in range(1,b):
            if a+b+np.sqrt(a**2+b**2)==n:
                return a*b*np.sqrt(a**2+b**2)