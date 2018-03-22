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

# P10
# 0.....
# 10!
# 1.....
# 2.....
# 3.....
# 4.....
# 5.....
# 6.....
# 7.....
# 8.....
# 9.....


#IDEA
#create definitions for lexicalPermutation3-10
# lP4 will call lP3 3 times, and so on

import factorial
import pdb

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
    for j in range(0, factorial.factorial(len(num)-1)):
      temp[j] = num[i] + temp[j]
    # add updated sub lists to current
    permutations += temp
    nextNum = nextNum[1:] + nextNum[0]
  return permutations


    # for 0123456789; len(num) = 10
    # 0(9! ways of the next digits) 0st : 362880 = 9! permutations with 0 starting
    # 1(9! ways of the next digits) 1st : 362881 - 725760 permutations with 1 starting
    # 2(9! ways of the next digits) 2nd : 725761 - 1088640 permutations with 2 starting
    #                                   : in the Project Euler example, the millionth number lies in this range
    # 3(9! ways of the next digits) 3rd
    # 4(9! ways of the next digits) 4th
    # ...

# finds the nth permutation of "num"
def find(num, n, perm = list(range(0,10))):
    print("PERM: " + str(perm))
    ret = ""
    num = str(num)
    if len(perm) == 1:
        val = str(perm[0])
        perm.pop(0)
        return val
    elif n<= 0:
        val = str(perm[0])
        perm.pop(0)
        return val + find(num[1:], 0, perm)
    # number of ways to keep the first digit, and change the others
    fact = factorial.factorial(len(num)-1)

    # updated value for fact
    temp = 0

    # place keeps track of whether 0th, 1st, 2nd, 3rd....
    place = 0
    # n = 1000000
    # place     0           1               2           3
    # fact = 1-362880, 362881-725760, 725761-1088640, 1088641-...
    # or   = 8!     ,   2*8!        ,   3*8!        ,   4*8!
    for i in range(1, len(perm)+1):
        temp = i * fact
        if temp >= n:
            place = i-1
            break
    # get the lower bound of that set
    #pdb.set_trace()
    temp -= fact
    # update return
    print("N: " + str(n))
    print("TEMP: " + str(temp))
    print("N-TEMP: " + str(n-temp))
    print("PLACE: " + str(place))
    ret += str(perm[place])
    # remove item from list
    perm.pop(place)
    # pass along the rest of the numbers, decrease n for n-1 digits
    ret += find(num[1:], n - temp, perm)
    return ret

"""
# finds the permutation @index
def find(index, num):
  num = str(num)
  if index-1 <= factorial.factorial(index-1) and index-1 >= 1:
    return lPn(num)[index-1]
  return "DID NOT FIND"
"""

done = False
while done == False:
  num = "0123456789"
  start = int(input("Start (inclusive): "))
  end = int(input("End (exclusive): "))

  print("List of permutations from index " + str(start) + " to " + str(end-1)
      + " with the number " + num[0:end])

  for i in range(start,end):
    print(lPn(num[0:i]))

  response = input("Again? ")
  if response[0].lower() == "n":
    done = True

print(factorial.factorial(int(input("Find Factorial of: "))))
#print(find("0123", 2))
print(find("0123456789", 1000000))
