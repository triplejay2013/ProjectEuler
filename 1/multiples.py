from time import *

def multipleSum(factor1, factor2, limit):
  total = 0
  for i in range(1,limit):
    if i%factor1== 0 or i%factor2 == 0:
      total+=i
  return total

print("""
    
Multiples of 3 and 5
Problem 1

  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

  Find the sum of all the multiples of 3 or 5 below 1000.

  Answer: 233168

  """)
while True:
  factor1 = int(input("Enter first Factor: "))
  factor2 = int(input("Enter second Factor: "))
  limit = int(input("Enter limit: "))
  start=clock()
  print("The multiple sum of {} and {} for numbers under {} is {}".format(factor1, factor2, limit,multipleSum(factor1,factor2,limit)))
  end = clock()
  print("Your program took {} seconds to run".format(end-start))
