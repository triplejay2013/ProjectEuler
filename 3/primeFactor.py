print("""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

""")

from time import clock as c
from math import sqrt

def sieve(limit):
    primes = set()
    s = [False] * (limit+1)
    for i in range(2, limit+1):
        if s[i]:
            continue
        primes.add(i)
        for j in range(i*i, limit + 1, i):
            s[j] = True
    return primes

primes = set()
while True:
    largest = 0
    try:
        limit = int(input("Enter number (600851475143 by default): "))
    except ValueError:
        limit = 600851475143
    if len(primes) == 0 or limit > max(primes): 
        primes = sieve(int(sqrt(limit)))
    start = c()
    for i in primes:
        if limit % i == 0:
            if i > largest:
                largest = i
            
    print("The largest prime factor of {} is {}".format(limit,largest))
    end = c()
    print("The program took {} seconds to run".format(end-start))

