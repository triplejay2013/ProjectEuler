# Digit factorials
# Problem 34 
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
from time import *

def factorial(n):
  if n <= 1:
    return 1
  return n*factorial(n-1)

def isDigitFact(num):
  tmp = str(num)
  total = 0
  for i in tmp:
    total += factorial(int(i))
  return total == num


while True:
  start = clock()
  print("Factorials from 0-5:")
  for i in range(0, 6):
    print(factorial(i))

  input("Is 145 a digit factorial?")
  if isDigitFact(145):
    print("YES")
  else:
    print("NO")

  facts = []
  try:
    limit = int(input("Enter limit: "))
  except ValueError:
    limit = 1000
  for i in range(3, limit):
    if isDigitFact(i):
      input("I: " + str(i))
      facts.append(i)
  print("Sum of all digit facts is: ")
  print(sum(facts))


  end = clock()
  input("The program took %f seconds to run" % (end - start))
