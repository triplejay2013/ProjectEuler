#
#A permutation is an ordered arrangement of objects. For example, 3124 is one
#possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
#are listed numerically or alphabetically, we call it lexicographic order. The
#lexicographic permutations of 0, 1 and 2 are:

# 1     2     3     4     5     6
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
#6, 7, 8 and 9?

#     1
# ...789 = num
#     2     3         4       5       6
#  ...798 ...879  ...897  ...978  ...987
# list of P3 [798,879,897,978,987]

#      2       3       4       5         6
#  ...6798 ...6879  ...6897  ...6978  ...6987 = P3


# i've exhaused all possiblities of 6### with P3
#     7     8       9         10        11
# ..7689  ..7698  ..7869  ..7896  ..7968  ..7986
#   12      13      14      15      16      17
# ..8679  ..8697  ..8769  ..8796  ..8967  ..8976
#     18    19      20      21      22      23
# ..9678  ..9687  ..9768  ..9786  ..9867  ..9876
# list of P4 [P3, ...

# P5
# ...56789
# ...5#### has been exhausted already
# needs to be done
# ...6####
# ...7####
# ...8####
# ...9####


#IDEA
#create definitions for lexicalPermutation3-10
# lP4 will call lP3 3 times, and so on

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

def factorial(num):
  ret = 1
  for i in range(2,num+1):
    ret *= i
  return ret

1234
# finds the permutation @index
def find(index, num):
  num = str(num)
  if index-1 <= factorial(index-1) and index-1 >= 1:
    return lPn(num)[index-1]
  return "DID NOT FIND"

print(lPn("012"))
print(lPn("01234"))

print(find(2,"0123"))
print(find(1000000, "0123456789"))

"""

# 0###
# 1###
# 2###
# 3###
def lP4(num):
  permutations = []

  nextNum = num
  # four possible variations of num[0]
  for i in range(0,4):
    temp = lP3(nextNum[1:])
    # add the four variations to the six variations of lP3
    for j in range(0,6):
      temp[j] = num[i] + temp[j]
    
    permutations +=temp
    nextNum = nextNum[1:] + nextNum[0]
  return permutations
  """
