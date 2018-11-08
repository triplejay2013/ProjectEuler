"""
Prime Permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?"""

from math import sqrt
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
for i in x:
    permutations = itertools.permutations(str(i))
    p=[]
    for j in permutations:
        p.append(int("".join(j)))
    if any(j in p for j in x):
        print("yes")
    for k in p:
        print(k)
    input()

# (3) Concatenate primes (in increasing order) to form 12-digit number
