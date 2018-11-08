from time import *
from math import sqrt

print("""

  Problem 2
  Even Fibonacci Numbers

  Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
  the first 10 terms will be:

  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

  By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of
  the even-valued terms.

  Answer: 4613732

  """)

cache = set()
#using memoization
def fib(n):
  try:
    result = int((((1+sqrt(5))**n)-(1-sqrt(5))**n)/((2**n)*sqrt(5)))
    cache[n] = result
    return result
  except OverflowError:
    if n in cache: return cache[n]
    if n < 1: return 0
    if n == 1 or n == 2: return 1
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result

def evenFib(n):
  fibs = []
  for i in range(1, n):
    val = fib(i)
    if val < n and val % 2 == 0: 
      fibs.append(i)
  return fibs

# Created with help from:
# https://www.mathblog.dk/project-euler-problem-2/
def fastFib(n):
  fib1 = 1
  fib2 = 1
  current = 0
  total = 0
  while current < n:
    if current%2 == 0:
      total+=current
    current = fib1+fib2
    fib2=fib1
    fib1=current
  return total
  
while True:
  limit = int(input("Enter limit: "))
  start=clock()
  print(fastFib(limit))
  # fibSeq = evenFib(limit)
  # print("The sum of all even-fib numbers with values less than {} is {}".format(limit, sum(fibSeq)))
  end=clock()
  print("The program took {} seconds to run".format(end-start))