# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
# 
# What is the largest n-digit pandigital prime that exists?
from time import *

def isPandigital(num):
  num = str(num)
  n = len(num)
  digits = [str(i) for i in range(1, n+1)]
  cnt = 1
  for i in num:
    for j in num[cnt:]:
      if i == j:
        return False
    try:
      digits.remove(i)
    except ValueError:
      return False
    cnt += 1
  if len(digits) == 0:
    return True
  return False

def primes(limit):
    sieve = [False] * limit
    for i in range(2,limit):
        if sieve[i]: continue
        yield i
        if i*i > limit: continue
        for j in range(i, limit, i):
            sieve[j] = True
    return sieve

while True:
  start = clock()
  limit = int(input("Enter limit: "))
  pan = []
  for i in primes(limit):
    if isPandigital(i):
      pan.append(i)
  if len(pan) == 0:
    print("Nothing found")
  else:
    print("The largest prime pandigital from 1-{} is {}".format(limit, max(pan)))
  end = clock()
  print("The program took {} seconds to run".format(end-start))
