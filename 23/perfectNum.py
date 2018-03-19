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
  for i in range(1, (num//2)+1):
    if num % i == 0:
      ret.append(i)
  return ret


def deficient(num):
  total = 0
  for i in properDivisors(num):
    total += i
  return True if total < num and total != num else False

def abundant(num):
  total = 0
  for i in properDivisors(num):
    total += i
  return True if total > num and total != num else False

var = 28
print("The Proper Divisors of " + str(var) + " are: " + str(properDivisors(var)))
print(str(var) + " is deficient? " + str(deficient(var)))
print(str(var) + " is abundant? " + str(abundant(var)))


total = []
# t_1 = ab1 + ab2
# add i to list if i cannot be written as two abundant sums
# if i and j are not abundant numbers, and i - j == 0, add to list
for i in range(1,28123): # represents positive integers, which are the sum of abundant_j and abundant_k
  for j in range(1, (i//2)+1): # represents abundant numbers up to half the total (i)
    for k in range(1, (i//2)+1): # represents abundant numbers up to half the total (i)
      if not abundant(j) or not abundant(k):
        total.append(j+k)
      elif abundant(j) and abundant(k)

# put into a set, and back to a list to remove duplicates
list(set(total))
#print sum of list
print("The sum of all non-abundant numbers is " + str(sum(total)))
