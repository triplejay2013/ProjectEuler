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
#returns DISTINCT factors of n
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

# Given a number n, calculate n+1, n+2,
# and add to list given that n,n+1 and n+1,n+2 have distinct primes
def consecutiveDistinctPrimes(n0):
    #pdb.set_trace()
    result = [n0]
    n0f=factor(n0)
    n1=n0+1
    n1f=factor(n1)
    # REF: https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
    # Checks if any contents match between the two lists
    # Considers only numbers with the same number of factors
    if not any(i in n0f for i in n1f) and len(n0f) == len(n1f):
        return result + consecutiveDistinctPrimes(n1)
    return result

#print(consecutiveDistinctPrimes(14))
#print(consecutiveDistinctPrimes(644))
print("Try numbers less than 150,000 for Project Euler solution")
n_distinct = int(input("Enter Number of factors to consider (>2): "))
for i in range(10,int(input("Enter Limit(>10): "))):
    if len(factor(i)) == n_distinct:
        x=consecutiveDistinctPrimes(i)
        if len(x) == n_distinct:
            print(x)
