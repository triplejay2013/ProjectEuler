"""
Prime Permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?"""

from math import sqrt
import pdb
import itertools

# (1) Generate four-digit primes
def primes_sieve(n):
    # Define boolean array, index denotes number. True, means prime, False
    # means not prime
    primes=[]
    not_prime = [True] * n
    not_prime[0] = not_prime[1] = False #0 and 1 are not prime

    # Tips on why i use enumerate
    # REF: http://book.pythontips.com/en/latest/enumerate.html
    for (i,isprime) in enumerate(not_prime):
        if isprime:
            primes.append(i)
            # See wiki page for explanation
            for n in range(i*i,n,i):
                not_prime[n] = False
    return primes

# n is a list of integers
# r is a range to restrict digits in the list
# digitStrip will remove any integers with digitCount > r or digitCount < r
# Digits with duplicate digits in sequence are also removed
def digitStrip(n,r):
    res = []
    for i in n:
        if not (len(str(i)) != r):
            if len(set(str(i))) == len(str(i)): # no duplicate digits exist
                res.append(i)
    return res

x=primes_sieve(9999)
x=digitStrip(x,4)

# (2) Iterate through primes, and determine if any permutations exist
#permutations = itertools.permutations()

# returns a list of permutations of number n
def permute(n):
    global x
    permutations = itertools.permutations(str(n))
    p=[]
    for j in permutations:
        i=int("".join(j))
        if i in x:
            p.append(i)
    return sorted(p)

# TODO: Need to meet third condition. All primes have same difference
def diffCheck(n):
    # Double for loop over list of primes
    # x = n[1] - n[0]
    # if n[i] + x in n, something

for i in x:
    j=permute(i)
    #j=diffCheck(j)
    print(j)

# (3) Concatenate primes (in increasing order) to form 12-digit number
