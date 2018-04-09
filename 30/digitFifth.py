# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
# 
#   1634 = 1^4 + 6^4 + 3^4 + 4^4
#   8208 = 8^4 + 2^4 + 0^4 + 8^4
#   9474 = 9^4 + 4^4 + 7^4 + 4^4
#   As 1 = 1^4 is not a sum it is not included.
# 
#   The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
#   Find the sum of all the numbers that can be written as the sum of fifth
#   powers of their digits.
from time import *

# eq is a list representation of an integer
def prettyPrint(eq, power=4):
  num = ""
  for i in eq:
    num += str(i)
  output = num
  output += " = "
  for i in eq:
    output += str(i) + "^" + str(power) + " + "
  # remove excess '+'
  output = output[0:len(output)-2]
  numInt = 0
  for i in eq:
    numInt += pow(i,power)
  if int(num) == numInt:
    output += " = " + num
    print(output)
    return True
  return False



def fourthPowerDigitSum(limit = 10000):
  total = 0
  # numbers 0-9 do nt have a power digit sum
  for i in range(10, limit):
    # put each digit of every number into this list
    num = [int(j) for j in str(i)]
    # print(num)
    if prettyPrint(num,4):
      total += i
  return total

def fifthPowerDigitSum(limit = 10000):
  total = 0
  for i in range(10, limit):
    num = [int(j) for j in str(i)]
    if prettyPrint(num, 5):
      total += i
  return total


while True:
  # start clock
  start = clock()

  limit = int(input("Enter Upper Bound: "))
  if limit < 10: 
    limit = 11
  print("\n\nFourth Power Digit Sum:")
  print(fourthPowerDigitSum(limit))
  # used limit of 1,000,000 to solve the problem
  print("\n\nFifth Power Digit Sum:")
  print(fifthPowerDigitSum(limit))

  # stop clock
  end = clock()
  print("The program ran for %f seconds" % (end-start))
