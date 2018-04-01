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

from decimal import *
from time import *

def recipCycle(num, limit = 10000):
    getcontext().prec = limit
    var = str(Decimal(1)/Decimal(num))
    #print(var)

    cycle = 1
    # .1666666666666666
    # .(142857)(142857)(142857)
    # check up to half the limit (after that, no pattern is guarenteed)
    while cycle < limit:
        # exclude "0." by starting at var[2]
        for i in range(2, limit):
            # a match is found ***NOT GUARENTEED TO REPEAT!!
            if var[i:i+cycle] == var[i+cycle:i+2*cycle] == var[i+2*cycle:i+4*cycle]:
                return cycle
        cycle += 1
    return 0
        

start = time()
maxVal = 0
den = 1
for i in range(1, 1000):
    var = recipCycle(i)
    if var > maxVal:
        maxVal = var
        den = i
        print("The current largest reccurence is " + str(maxVal) + " at 1/" + str(i))

print(recipCycle(den))
print("The largest recurring cycle was " + str(maxVal) + " long and was with the number 1/" + str(den))

getcontext().prec = 982
print(Decimal(1)/Decimal(983))
print(recipCycle(983))
end = time()
print("The program took " + str(start-end) + " seconds to run")
