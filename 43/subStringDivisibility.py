# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.
# 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:
# 
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
from time import *

def factorial(num):
  if num == 0:
    return 1
  elif num < 0:
    return 0
  ret = 1
  for i in range(2,num+1):
    ret *= i
  return ret

# Lexical permutations
def lP3(num):
  permutations = []
  temp = num

  # can combine 3 #'s in 6 ways (3)*(2)*(1)
  temp = num[0] + num[1] + num[2]
  permutations.append(temp)
  temp = num[0] + num[2] + num[1]
  permutations.append(temp)
  temp = num[1] + num[0] + num[2]
  permutations.append(temp)
  temp = num[1] + num[2] + num[0]
  permutations.append(temp)
  temp = num[2] + num[0] + num[1]
  permutations.append(temp)
  temp = num[2] + num[1] + num[0]
  permutations.append(temp)
  return permutations

def lPn(num):
  num = str(num)
  if len(num) < 3:
    return "INVALID NUMBER"
  if len(num) == 3:
    return lP3(num)

  permutations = []
  nextNum = num
  # n possible variations of num[0]
  for i in range(0,len(num)):
    if len(nextNum[1:]) == 3:
      temp = lP3(nextNum[1:])
    else:
      temp = lPn(nextNum[1:])
    # add the n first number variations to the (n-1)! variations of lP(n-1)
    for j in range(0, factorial(len(num)-1)):
      temp[j] = num[i] + temp[j]
    # add updated sub lists to current
    permutations += temp
    nextNum = nextNum[1:] + nextNum[0]
  return permutations

def isPandigital(num):
  num = str(num)
  n = len(num)
  unique = []
  digits = [str(i) for i in range(n)]
  for i in num:
    if i not in unique:
      unique.append(i)
    else: return False
    try:
      digits.remove(i)
    except ValueError:
      return False
  return len(digits) == 0

while True:
  if isPandigital(1406357289): print("YEAH")
  else: print("NO")
  input("Enter to start: ")
  start = clock()
  print("Beginning generation of all possible 0-9 digit pandigitals")
  pandigitals = lPn("0123456789")
  subStringPan = []
  found = False
  print("Starting search for special pandigitals")
  for pandigital in pandigitals:
    primes = [0,2,3,5,7,11,13,17]
    for j in range(1, len(pandigital)-2):
      tmp = int(str(pandigital[j]) + str(pandigital[j+1]) + str(pandigital[j+2]))
      if tmp % primes[j] != 0:
        found = False
        break
      else:
        found = True
    if found:
      subStringPan.append(int(pandigital))

  end = clock()
  print("The program took {} seconds to run".format(end-start))
  input("DONE! (Enter to continue...)")
  print(subStringPan)
  print("sum of substring pandigitals is {}".format(sum(subStringPan)))

