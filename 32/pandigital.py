# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is
# 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can
# be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.
from time import *

# formats an equation into a single number to check if pandigital
# ie 39 x 186 = 7254 => 391867254
def formatEq(eq):
  return 0

def isPandigital(num):
  num = str(num)
  n = len(num)
  # used to make sure each digit is used
  digits = [str(i) for i in range(1, n+1)]
  cnt = 1
  # used to make sure each digit is unique
  # if i and j are the same, then digits are not unique
  for i in num:
    for j in num[cnt:]:
      if i == j:
        return False
    try:
      digits.remove(i)
    except ValueError:
      return False
    cnt += 1
  # true if all digits were used
  # and if it has used all values of num (return False, handled above)
  if len(digits) == 0:
    return True
  return False

while True:
  start = clock()
  print("YES") if isPandigital(15234) else print("NO")
  limit = int(input("Enter limit (inclusive): "))

  total = []
  for i in range(1,limit+1):
    # starting at i avoids reciprocal identities "1 X 2 = 2 and 2 X 1 = 2"
    for j in range(i, limit+1):
      temp = str(i) + str(j) + str(i*j)
      if isPandigital(temp) and len(temp) == 9:
        print("%d x %d = %d" % (i,j,i*j))
        total.append(i*j)

  print("Removing duplicate products")
  total = list(set(total))
  print(total)
  print("Sum of all pandigital #'s with digits 1-9: %d" % (sum(total)))
  end = clock()
  print("The program took %f seconds to run" % (end-start))
