import pdb
# of times
# Non-abundant sums
# Problem 23 
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of
# two abundant numbers.


def properDivisors(num):
  ret = []
  for i in range(1, int(num/2)+1):
    if num % i == 0:
      ret.append(i)
  return ret


def deficient(num):
  myList = properDivisors(num)
  total = 0
  for i in myList:
    total += i
  return True if total < num and total != num else False

def abundant(num):
  myList = properDivisors(num)
  total = 0
  for i in myList:
    total += i
  return True if total > num and total != num else False

var = int(input("enter a number: "))

#DEBUG
pdb.set_trace()

abun_nums = []
for i in range(1,var):
  if abundant(i):
    abun_nums.append(i)
#print(abun_nums)

if var < 1000:
  print("The Proper Divisors of " + str(var) + " are: " + str(properDivisors(var)))
  print(str(var) + " is deficient? " + str(deficient(var)))
  print(str(var) + " is abundant? " + str(abundant(var)))

print("\nstart calculating Non-abundant number sums\n")

nums = []
counter = 0
for i in range(1,var):
  if i % 1000 == 0:
    counter += 1
    print(str(counter) + " ")
  if i in abun_nums:
    for j in range(1, var):
      if j in abun_nums:
        #DEBU
        pdb.set_trace()
        nums.append(i+j)

# put into a set, and back to a list to remove duplicates
list(set(nums))
#print(abun_nums)

# create list of non-abundant numbers from list of abundant numbers
total = []
for i in range(1, nums[len(nums)-1]):
  if i not in nums:
    total.append(i)

#print sum of list
#print(total)
print("The sum of all non-abundant numbers less than " + str(var) + " is " + str(sum(total)))
