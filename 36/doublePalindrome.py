# The decimal number, 585 = 1001001001 base2 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
from time import *

# helper function
def _isPalindrome(num, start, end):
  if start >= end: return True
  if num[start] == num[end]:
    return _isPalindrome(num, start+1, end-1)
  return False

def isPalindrome(num):
  return _isPalindrome(str(num), 0, len(str(num))-1)

# converts to binary *removes '0b'*
def binary(num):
  return int(bin(num)[2:])

# converts to decimal
def decimal(num):
  num = "0b" + str(num)
  return int(num, 2)
  

while True:
  start = clock()
  
  # test palindrome function
  if isPalindrome("racecar"): print("YES")
  else: print("NO")
  if isPalindrome("12345678987654321"): print("YES")
  else: print("NO")

  # test radix conversions
  if binary(42) == 101010: print("YES")
  else: print("NO")
  if decimal(10010) == 18: print("YES")
  else: print("NO")

  # solve project euler
  limit = int(input("Enter limit: "))
  palindromic = []
  palindromic_bin = []
  for i in range(limit):
    if isPalindrome(i) and isPalindrome(binary(i)):
      palindromic.append(i)
      palindromic_bin.append(binary(i))

  print(palindromic)
  print(palindromic_bin)
  print("The sum of all palindromic numbers is: %d" % (sum(palindromic)))
  end = clock()
  input("The program took %f seconds to run" % (end - start))
