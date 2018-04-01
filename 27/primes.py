from math import *
from pdb import * #set_trace()

def primes(limit):
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


for i in primes(100):
    #print("OUTSIDE")
    print(i)
for i in primes(100):
    #print("OUTSIDE")
    print(i)
