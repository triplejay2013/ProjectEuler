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

def sieve(limit):
    a= [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

# Recursively fine factors
# c - number to find factors of
# n - number of factors to find (default 2)
def factor(c):
    ret=(c,)
    if is_prime(c): return ret+(-1,-1) #if prime, no factors exist
    return ret + _factor(c)

# c - composite number
# f - factor
def _factor(c,f=2): # finds the next factor for c
    for i in range(f,c): # continue search for distinct factors
        if is_prime(i) and c%i==0: # if i is a prime factor
            return (f,)+_factor(c,i+1) # add to tuple
        f+=1 # else try a different factor
    return () #once f is greater than c, return empty tuple. Base case

# n MUST be at least a 2-tuple
# (p)retty (print)
def pprint(n):
    if len(n) <= 1: return
    toPrint=""
    toPrint += "{} = ".format(n[0])
    for i in range(1,len(n)):
        toPrint+="{} x ".format(n[i])
    
    toPrint=toPrint[:len(toPrint)-2] # remove trailing 'x '
    print(toPrint)

# (t)uple (L)ist
# TODO print out only tuples of interest
def distinctPrimeFactors(tL):
    for i in range(1,len(tL)):
        p=False # (p)rint flag
        for j in range(len(tL[i])): # look for consecutive distinct factors
            if tL[i-1][j] in tL[i]: # not distinct prime
                f=False
                tL[i-1] = ()
                break
            else: 
                f=True
        if f:
            print("\nDISTINCT")
            for j in tL: # print consecutive distinct factors
                pprint(j)
    print("END\n")


from time import clock
while True:
    l=int(input("Enter limit of factors to generate: "))
    mi=int(input("Enter minimum factor tuple length: "))
    start=clock()
    tL=[] # (t)uple (L)ist
    for i in range(1,l):
        c=factor(i)
        # Add only similar-length tuples
        # AND add only valid tuples
        if mi == len(c)-1 and c[1] != -1: 
            tL.append(c)

    for i in tL:
        print(i)
    # distinctPrimeFactors(tL) #broken

    print("The program took {} seconds to run".format(clock()-start))
