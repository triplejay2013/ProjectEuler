# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
# 
# How many circular primes are there below one million?
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

def isCircPrime(num, primes=eratosthenes(100)):
  num = str(num)
  circularPrimes = []
  # single digit case
  if len(num) == 1:
    return True if int(num) in primes else False

  # n digit case
  for i in range(len(num)):
    if int(num) in primes: 
      num = num[1:] + num[0]
    else: 
      return False
  return True


while True:
  start = clock()
  limit= int(input("Enter limit of primes to calculate: "))
  primes = eratosthenes(limit)
  if len(primes) <= 50:
    print(primes)

  # circular prime calculation
  input("Press Enter to start Circular Prime Calculation")
  circularPrimes = []
  for i in range(limit):
    if isCircPrime(i, primes):
      circularPrimes.append(i)

  print("The Circular Primes from 1 to %d are: " % (limit))
  print(circularPrimes)
  print("There are %d circular sums from 1 to %d:" % (len(circularPrimes), limit))
  end = clock()
  print("The program took %f seconds to run" % (end-start))
