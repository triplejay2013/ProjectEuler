# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 
#   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#   How many different ways can £2 be made using any number of coins?
from time import *


# 1 way to break down 2p
#   1p + 1p
# 2 ways to break down 3p
#   1(2p) + 1(1p)
#   4(1p)
# 3ways to break down 4p
#   2(2p)
#   1(2p) + 3(1p)
#   4(1p)
# 5 ways to break down 5p
#   1(5p)
#   2(2p) + 1(1p)
#   1(2p) + 3(1p)
#   0(2p) + 5(1p)


# With help of math blog....
# https://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/

# determines how many combinations exist to break the amount given
# amount = coin value to break
def coinSums(amount):
    coins = [1,2,5,10,20,50,100,200]
    combinations = [0] * amount
    combinations.append(0)
    combinations[0] = 1
    for i in range(0, len(coins)):
        for j in range(coins[i], amount+1):
            combinations[j] += combinations[j-coins[i]]
    return combinations[len(combinations)-1]

def coinSums_bruteForce(amount):
    combinations = 0
    for a in range(amount, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                combinations += 1
    return combinations
        
while True:
    # start clock
    start = clock()

    coin = int(input("Enter value to break: "))
    print("\nThere are %d ways to break %d" % (coinSums(coin), coin))

    print("\nBrute Force: There are %d ways to break %d" % (coinSums_bruteForce(coin), coin))

    # stop clock
    end = clock()
    print("The program took %f seconds to run" % (end - start))
