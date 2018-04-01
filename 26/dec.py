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


def recurringCycleLength(d = 2):
    seqLen = 0

    for i in range(1000, 1 , -1):
        if seqLen >= i:
            break

        remainders = [0] * i
        value = 1
        pos = 0

        while remainders[value] == 0 and value != 0:
            remainders[value] = pos
            value *= 10
            value %= i
            pos += 1

        if pos - remainders[value] > seqLen:
            seqLen = pos - remainders[value]

    return seqLen


def main():
    # CLOCK init
    start = time()

    # get a denominator and print out the recurring cycle length
    d = int(input("Enter denominator:1/"))
    getcontext().prec = 6
    print("1/%d = %f" % (d, (Decimal(1)/Decimal(d))))
    print("1/%d has a recurring cycle length of %d" % (d, recurringCycleLength(d)))

    # CLOCK stuff
    print("Total time was %d seconds" % (time()-start))

main()

