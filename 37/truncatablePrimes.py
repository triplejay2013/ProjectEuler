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
    if not isTruncPrime(i):
      sieve[i] = True
    if sieve[i]:
      continue
    for j in range(i*2, n+1, i):
        sieve[j] = True
    primes.append(i)
  return primes


"""
def truncatablePrime(num, primes = eratosthenes(10000)):
  if len(str(num)) <= 1:
    return False
  tmp = str(num)
  while len(tmp) > 0:
    if int(tmp) not in primes:
      return False
    tmp = tmp[1:]

  tmp = str(num)
  while len(tmp) > 0:
      if int(tmp) not in primes:
        return False
      tmp = tmp[:len(tmp)-1]
  return True

while True:
  start = clock()
  """

"""
  # test truncatable Prime
  print("IS 3797 a truncatable Prime?")
  if truncatablePrime(3797): print("YES")
  else: print("NO")
  """

while True:
  limit = int(input("Enter max limit: "))
  print("Working on now:")
  print(eratosthenes_trunc(limit))

"""
  # Solve Project Euler Problem
  limit = int(input("Enter number of truncatable primes you want to find: "))
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

  print("The sum of all %d truncatable prime(s) is %d" % (limit, sum(tp)))
  end = clock()
  print("The program took %f seconds to run" % (end-start))
"""

