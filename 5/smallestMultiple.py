print("""

# Smallest Multiple
## Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

Answer: 232792560
""")

from time import *

def smallestMultiples(limit, r):
    sM = 1
    nums = [int(i) for i in range(r, 1, -1)]
    for i in range(r, limit, r):
        flag = True
        for j in nums:
            if i%j != 0:
                flag = False
                break
        if flag:
            return i
    return 0

while True:
    start = clock()
    try:
        limit = int(input("Enter Limit (5000 by default): "))
        r = int(input("Enter Range (10 by default): "))
    except ValueError:
        print("Your expected answer is: 2520")
        r = 10
        limit = 5000

    print("Answer: ", end="")
    print(smallestMultiples(limit, r))
    print("The program took {} seconds to run".format(clock()-start))
