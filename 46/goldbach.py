"""Goldbach's other conjecture
Problem 46 
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""

# Composite Numbers
"""A composite number is a positive integer that can be formed by multiplying two smaller positive integers. Equivalently, it is a positive integer that has at least one divisor other than 1 and itself.[1][2] Every positive integer is composite, prime, or the unit 1, so the composite numbers are exactly the numbers that are not prime and not a unit.[3][4

REF: https://en.wikipedia.org/wiki/Composite_number"""

# Miller-Rabin primality test
# REF: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
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


def isOdd(n):
    return n%2!=0

# 2x1^2
# 2x2^2
def twiceSquare(n):
    return 2*(n**2)

def composites(n):
    ret=(n,)
    # In both for loops, n is the largest possible value (finding sum, sum of n+n is always > n
    for i in range(2,n):
        if is_prime(i):
            for j in range(1,n):
                _try=i+twiceSquare(j)
                if _try>n: break
                if _try==n:
                    return ret+(i,"2x{}^2".format(j))
    x=(-1,"None")
    return ret+x

# n - expected to be 3-tuple
def pprint(n):
    print("{} = {} + {}".format(n[0],n[1],n[2]))

"""
pprint(composites(9))
pprint(composites(15))
pprint(composites(21))
pprint(composites(25))
pprint(composites(27))
pprint(composites(33))
"""

from time import clock

l=int(input("Enter limit: "))
myList=[int(x) for x in range(l) if not is_prime(x) and isOdd(x)]
start=clock()
for i in myList:
    x=composites(i)
    if x[1] == -1:
        pprint(composites(i))
        break
    pprint(composites(i))

print("Program took {} seconds to run".format(clock()-start))
