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
import pdb

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
    return list(set(factors[1:])) # returns distinct factors
    # returns [f1,f2,f3,...,fk]

n_distinct = 4
flag=False
for i in range(15,int(input("Enter Limit: "))):
    prev=factor(i-1) #14
    curr=factor(i)   #15
    for j in prev:
        if j in curr:
            flag=False
            break
        else: flag=True
    if flag and (len(prev)==len(curr)==n_distinct):
        print("{} and {} have {} distinct primes".format(i-1,i,n_distinct))
        print("\tprev:{}\tcurr:{}".format(prev,curr))
