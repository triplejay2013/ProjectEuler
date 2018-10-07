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

# Miller-Rabin primality test
# REF: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
# Says that 1 is prime.....
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
# Global values
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]



# Recursively fine factors
# f - number to find factors of
# n - number of factors to find (default 2)
# m - most recent found factor
def factor(f,n=2):
    ret=(f,)
    if is_prime(f): return ret+(-1,-1)
    return ret + _factor(f,n)

def _factor(f,n=2,m=1):
    if n==0: return ()
    for i in range(m+1,f):
        if is_prime(i):
            j=_factor(f,n-1,m) # TODO Start here - implementing factor2() using recursion
            _try=i*j
            if _try>f: break
            if _try==n: return (i,j)

            return _factor(f,n-1,m)+(i,)

def factor2(n):
    ret=(n,)
    if is_prime(n): return ret+(-1,-1)
    for i in range(n):
        if is_prime(i):
            for j in range(i+1,n):
                if is_prime(j):
                    _try=i*j
                    if _try>n: break
                    if _try==n: return ret+(i,j)
    return ret+(-1,-1)

# n MUST be a 3-tuple
def pprint(n):
    print("{} = {} x {}".format(n[0],n[1],n[2]))

from time import clock
l=int(input("Enter limit: "))
start=clock()
for i in range(1,l):
    x=factor(i)
    print(x)
    #if x[1] != -1:
    #    pprint(x)

print("The program took {} seconds to run".format(clock()-start))
