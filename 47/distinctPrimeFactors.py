"""Distinct primes factors
Problem 47 
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?"""

from math import sqrt

# Returns a list
# [n, f1, f2,.., fk]
# Where n is the number factored
# and fi is the factor of n
# REF: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
def factor(n):
    # make positive
    factors = [n]
    if n<0: 
        n*=-1
        factors.append(int(-1))
    # No prime factors will be considered for 1,0
    if n<=1: return factors
    #Print the number of 2's that divide n
    while n%2==0:
        #print(2)
        factors.append(int(2))
        n/=2

    # N must be odd at this point, so we can skip an element
    for i in range(3,int(sqrt(n)+1),2):
        while n%i == 0:
            #print(i)
            factors.append(int(i))
            n/=i
    # This condition is to handle the case when n is a 
    # prime number greater than 2
    if n>2:
        #print(n)
        factors.append(int(n))
    return factors

# List of distinct priems
dprimes=[]
# number of distinct prime factors to consider
n_distinct=2
flag=False
for i in range(3,100):
    x=factor(i-1) #14,2,7
    y=factor(i)   #15,3,5
    for j in x: # Loop through factors of i-1
        if (j not in y) and len(x)-1 == n_distinct and len(y)-1 == n_distinct:
        # if factors of i-1 are not in factors of i, then distinct
        # len() -1 to account for n in 0th location.
            flag = True
        else: flag = False
    if flag:
        # Skip lists with duplicate factors
        #if len(set(x)) != len(x): continue
        #if len(set(y)) != len(y): continue
        dprimes.append(x)
        dprimes.append(y)
    flag=False

for i in dprimes:
    print(i)
            
