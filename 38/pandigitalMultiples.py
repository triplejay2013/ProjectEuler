# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
# call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
# 5, giving the pandigital, 918273645, which is the concatenated product of 9 and
# (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?
from time import *

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

  end = clock()
  input("The program took %f seconds to run" % (end - start))
