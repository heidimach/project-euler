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
    return p_large

def special_pythagorean_triplet(n=1000):
    B=n
    for b in range(2,B):
        for a in range(1,b):
            if a+b+np.sqrt(a**2+b**2)==n:
                return a*b*np.sqrt(a**2+b**2)

def summation_of_primes(n=10):
    i=2
    primes=2
    L=[j for j in range(2,int(n)) if j%i!=0]
    while i < n:
        if len(L)>0:
            primes=primes+L[0]
            i=L[0]
        else:
            break
        L=[j for j in L if j%i!=0]
    return primes

def largest_product_in_grid(n=4):
    grid=np.array([[int(num) for num in row.split(' ')] for row in """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48""".split('\n    ')])
    
    y=0
    x=0
    max_dir=0
    
    while y<grid.shape[0]:
        while x<grid.shape[1]:
            hori=0
            vert=0
            diag_up=0
            diag_down=0
                
            if x+n-1<grid.shape[1] and y+n-1<grid.shape[0]:
                dgn_down=[]
                dgn_up=[]
                for i in range(n):
                    dgn_down.append(grid[y+i][x+i])
                    dgn_up.append(grid[n+y-i-1][x+i])
                diag_down=np.prod(dgn_down)
                diag_up=np.prod(dgn_up)
                    
            if y<grid.shape[0] and x+n-1<grid.shape[1]:
                hori=np.prod(grid[y][x:x+n])
                
            if y+n-1<grid.shape[0] and x<grid.shape[1]:
                vert=np.prod(grid.T[x][y:y+n])
                
            if max_dir<max(hori,vert,diag_down,diag_up):
                max_dir=max(hori,vert,diag_down,diag_up)
            
            x+=1
        x=0
        y+=1
    
        
    return max_dir

print(largest_product_in_grid(n=4))