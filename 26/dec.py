# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# www.mathblog.dk/....

from time import *
from decimal import *
from pdb import *

# this function is the same as below, 
# the only difference is we remove the tracking of remainders
# we can do this because the first remainder calculated will always be
# a '1'. ex: 1%7, 1%8, 1%x = 1 ALWAYS. As soon as we perform that calculation
# the same way again, the cycle will repeat
"""
def cycleLength(b):
    a = 1
    t = 0

    a = a * 10 % b
    t+=1

    while a != 1:
        a = a * 10 % b
        t+=1
    return t
"""

def cycleLength(b):
    # create a dictionary which has unique key-value pairs
    # this keeps track of the remainders while calulating the decimal series

    # this column
    # |
    # V
    # 1 / 7 = 0.14285714285714285
    # 10 / 7 = 1.4285714285714286
    # 30 / 7 = 4.285714285714286
    # 20 / 7 = 2.857142857142857
    # 60 / 7 = 8.571428571428571
    # 40 / 7 = 5.714285714285714
    # 50 / 7 = 7.142857142857143

    # ** Repeats below, the number of steps til this repetition is 6
    # the modulus will calculate numbers 0-6 in infinte ways...
    # but as soon as it calculates using the same remainder (shown in the left column)
    # then we are repeating, because all following calculations will be the same
    # the calucaltion of 10 / 7 will always result in 30 / 7...and so on, and so once we detect
    # a remainder that has been detected before, then we know that the pattern repeats from that point on
    # without a need to conintue checking. Because the calculation process has essentially started from where we started


    # 10 / 7 = 1.4285714285714286
    # 30 / 7 = 4.285714285714286
    # 20 / 7 = 2.857142857142857
    # 20 / 7 = 2.857142857142857
    # 60 / 7 = 8.571428571428571
    # 40 / 7 = 5.714285714285714
    # 50 / 7 = 7.142857142857143

    rem = {}
    # remainder 'a' starts at 1
    a = 1
    # length will start at 0
    t = 0

    # do this once
    rem[a] = t
    a = a % b * 10
    t+=1

    # continue until 'a' is calculated again
    while  a not in rem:
        #set_trace()
        rem[a] = t
        a = a % b * 10
        t+=1
    return t - rem[a]

def printCycle(d = 2):
    a = 1
    b = d
    digits = 10
    for i in range(0, digits):
        n = a/b
        print(str(a) + " / " + str(b) + " = " + str(n))
        a = a % b * 10



def main():

    d = 1
    while d > 0 :
        # get a denominator and print out the recurring cycle length
        d = int(input("Enter denominator: 1/"))
        if d <= 1:
            break
        getcontext().prec = 6
        print("1/%d = %f" % (d, (Decimal(1)/Decimal(d))))
        printCycle(d)
        print("1/%d has a recurring cycle length of %d" % (d, cycleLength(d)))

        # CLOCK init
        limit = input("Enter limit: ")
        start = time()
        print("find max recurring cycle for numbers less than " + limit)
        big = 0
        counter = 2
        num = 2
        while counter < int(limit):
            tmp = cycleLength(counter)
            if tmp > big:
                big = tmp
                num = counter
            counter +=1

        print("The biggest recurring cycle is for %d at a length of %d" % (num, big))
        # CLOCK stuff
        print("Total time was %d seconds" % (time()-start))

main()

