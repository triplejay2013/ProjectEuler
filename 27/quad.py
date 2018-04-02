# Euler discovered the remarkable quadratic formula:
# 	n^2+ n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive integer values 0<= n <= 39. However, when
# n= 40, 40^2 + 40 + 41 = 40(40+1) + 41 is divisible by 41, and certainly when n= 41, 41^2 + 41 + 41 is clearly divisible by 41.
# 
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The
# product of the coefficients, -79 and 1601, is -126479
# 
# Considering quadratics of the form:
# 	n^2 + an + b, where |a| < 1000 and |b| <= 1000
# 
# 	where |n| is the modulus/absolute value of n
# 	e.g. |11| = 11 and |-4| = 4
# 
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for 
# consecutive values of n, starting with n = 0 

from math import *
from time import *
from pdb import * #set_trace()

def prime_generator(limit):
    sieve = [False] * limit

    for i in range(2,limit):
        if sieve[i]: continue
        #print("INSIDE")
        yield i
        # look up generators and 'yield'
        # basically, this returns a generator that performs 'i', or just gives back the value of i
        # once this function is called again, then it continues from this point until it reaches 
        # the next yield, and returns that
        # uncomment my "inside" "outside" comments to see that in action

        # generators are like iterators...that don't keep track of where they are. They just generate
        # the next number in the sequence and forget everything else.
        if i*i > limit: continue
        for j in range(i, limit, i):
            sieve[j] = True
    return sieve

def is_prime(num = 1, limit=100000):
    sieve = [False] * limit
    primes = []

    for i in range(2,limit):
        if sieve[i]: continue
        primes.append(i)
        if i*i > limit: continue
        for j in range(i, limit, i):
            sieve[j] = True
    return num in primes

# finds coefficients for quadratic expression that prodcues the max number of primes for
# consecutive values of n 
# form: n^2 + an + b, 
#   where |a| < 1000 and |b| <= 1000
def quadraticPrimeEquation():
    # Start the CLOCK
    start = time()
    # Track the length of primes generated from quadratic equation
    maxlen = 0
    # Tracks max a coefficient
    maxA = 0
    # Tracks max b coefficient
    maxB = 0
    
    # The following for loops consider only prime iterators 
    for a in range(0,1000):
        for b in range(0,a):
            primes = []
            for n in range(10000000):
                # tries the given quadratic equation with values of 0 < n < 10000000
                res = (n**2) + a*n + b
                # check for consecutive prime
                if is_prime(res):
                    primes.append(res)
                # if the next number is not prime, then we are done finding consecutive primes
                else:
                    # print which equation we were considering
                    print("\nEQUATION:\n\tn^2 + " + str(a) + "n + " + str(b))
                    # Check if any primes were found
                    if len(primes) == 0:
                        print("No primes found")
                    # if not, print out how many were found
                    else:
                        print("%d primes found from 0 to %d" % (len(primes), len(primes)-1))
                    if len(primes) > maxlen:
                        maxlen = len(primes)
                        maxA = a
                        maxB = b
                        input("CURRENT MAXLEN:\n\t" + str(maxlen))
                    break
    print("maxA = %d\tmaxB = %d" % (maxA, maxB))
    print("Product of maxes is: %d" % (maxA*maxB))
    print("Process took $d seconds" % (time() - start))

quadraticPrimeEquation()
