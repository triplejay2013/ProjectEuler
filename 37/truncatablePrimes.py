# The number 3797 has an interesting property. Being prime itself, it is possible
# to continuously remove digits from left to right, and remain prime at each
# stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
# 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
# 
# NoTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from time import *


def eratosthenes(n):
  sieve = [False] * (n+1)
  primes = []
  for i in range(2, n+1):
    if sieve[i]:
      continue
    for j in range(i*2, n+1, i):
      sieve[j] = True
    primes.append(i)
  return primes

"""
erat = eratosthenes(10000)

def isTruncPrime(num):
  if len(str(num)) <= 1: return False
  global erat
  tmp = str(num)
  while len(tmp) > 0:
    if int(tmp) not in erat:
      return False
    tmp = str(tmp)[:len(str(tmp))-1]
  tmp = str(num)
  while len(tmp) > 0:
    if int(tmp) not in erat:
      return False
    tmp = str(tmp)[1:]
  return True

def eratosthenes_trunc(n):
  sieve = [False] * (n+1)
  primes = []
  for i in range(2, n+1):
    if not isTruncPrime(i): sieve[i] = True
    if sieve[i]:
      continue
    for j in range(i*2, n+1, i):
        sieve[j] = True
    primes.append(i)
  return primes
"""

prime = eratosthenes(1000000)

def truncatablePrime(num):
  global primes
  if len(str(num)) <= 1:
    return False
  tmp = str(num)
  while len(tmp) > 0:
    if int(tmp) not in prime:
      return False
    tmp = tmp[1:]

  tmp = str(num)
  while len(tmp) > 0:
      if int(tmp) not in prime:
        return False
      tmp = tmp[:len(tmp)-1]
  return True

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

while True:
  start = clock()

  # test truncatable Prime
  print("IS 3797 a truncatable Prime?")
  if truncatablePrime(3797): print("YES")
  else: print("NO")

  # Solve Project Euler Problem
  
  limit = int(input("Enter number of truncatable primes you want to find: "))
  if limit > 11: limit = 11
  if limit <= 0: limit = 1
  tp = []
  cnt = 0
  for i in primes(1000000):
    if cnt == limit: break
    if truncatablePrime(i):
      print("%d is a truncatable prime" % (i))
      cnt+=1
      tp.append(i)
  """
  print("Generating Sieve")
  primes = eratosthenes(1000000)
  if limit > 11: limit = 11
  if limit <= 0: limit = 1
  tp = []
  cnt = 0
  i = 23
  print("Calculating truncatable Primes")
  while cnt < limit:
    if truncatablePrime(i, primes):
      print("%d is a truncatable prime" % (i))
      cnt+=1
      tp.append(i)
    i += 2

  """
  print("The sum of all %d truncatable prime(s) is %d" % (limit, sum(tp)))
  end = clock()
  print("The program took %f seconds to run" % (end-start))

