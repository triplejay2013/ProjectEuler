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

def printPandigital(num=9, digitMax =9):
  print("{} and (".format(num), end="")
  product = ""
  cnt = 0
  for i in range(1,digitMax+1):
    if len(str(i*num) + product) > digitMax:
      cnt = i
      break
    product += str(i*num)
  for i in range(1,cnt):
    print("{}, ".format(i), end="")
  print(") = ", end="")
  print(product)
  return product

def pandigitals(num=9, digitMax = 9):
  product = ""
  cnt = 0
  for i in range(1,digitMax+1):
    if len(str(i*num) + product) > digitMax:
      cnt = i
      break
    product += str(i*num)
  return product
# ANALYSIS - to optimize my search
"""
I can only have 9 digit numbers
let us consider a static integer from 1-n
1 and (1,2,3,4,5,6,7,8,9) = 123456789 OK
2 and (1,2,3,4,5,6,7) = 2468101214  NOPE
3 and (1,2,3,4,5,6) = 369121518  NOPE
4 and (1,2,3,4,5,6,7) = 481216202 NOPE
5 and (1,2,3,4,5,6,7) = 1020304050 NOPE
6 and (1,2,3,4,5,6,7) = 612182430 NOPE
7 and (1,2,3,4,5,6,7) = 714212835 NOPE
8 and (1,2,3,4,5) = 816243240 NOPE
9 and (1,2,3,4,5) = 918273645 OK

"""
# end analysis


while True:
  pandigital = []
  start = clock()
  limit = int(input("Enter limit: "))
  for i in range(1,limit):
    if isPandigital(pandigitals(i)):
      printPandigital(i)
      pandigital.append(pandigitals(i))
    
  print("The max pandigital is {}".format(max(pandigital)))
  end = clock()
  print("The program took %f seconds to run" % (end - start))
