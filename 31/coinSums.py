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
# 5 ways to break down 6p
#   1(5p) + 1(1p)
#   3(2p)
#   2(2p) + 2(1p)
#   1(2p) + 4(1p)
#   6(1p)
# 6 ways to break down 7p
#   1(5p) + 1(2p)
#   1(5p) + 2(1p)
#   3(2p) + 1(1p)
#   2(2p) + 3(1p)
#   1(2p) + 5(1p)
#   7(1p)
# 7 ways to break down 8p
#   1(5p) + 1(2p) + 1(1p)
#   1(5p) + 3(1p)
#   4(2p)
#   3(2p) + 2(1p)
#   2(2p) + 4(1p)
#   1(2p) + 6(1p)
#   8(1p)
# ways to break down 9p
# 9 ways to break down 10p
#   2(5p)
#   1(5p) + 2(2p) + 1(1p)
#   1(5p) + 1(2p) + 3(1p)
#   0(5p) + 5(2p) + 0(1p)
#   0(5p) + 4(2p) + 2(1p)
#   0(5p) + 3(2p) + 4(1p)
#   0(5p) + 2(2p) + 6(1p)
#   0(5p) + 1(2p) + 8(1p)
#   0(5p) + 0(2p) + 10(1p)
# 41 ways to break down 20p
#   1(20p) + 0(10p) + 0(5p) + 0(2p) + 0(1p)
#           Recurse?
#   0(20p) + 2(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(20p) + 1(10p) + 2(5p) + 0(2p) + 0(2p)
#   0(20p) + 1(10p) + 1(5p) + 2(2p) + 1(2p)
#   0(20p) + 1(10p) + 1(5p) + 1(2p) + 3(2p)
#   0(20p) + 1(10p) + 1(5p) + 0(2p) + 5(2p)
#   0(20p) + 1(10p) + 0(5p) + 5(2p) + 0(2p)
#   0(20p) + 1(10p) + 0(5p) + 4(2p) + 2(2p)
#   0(20p) + 1(10p) + 0(5p) + 3(2p) + 4(2p)
#   0(20p) + 1(10p) + 0(5p) + 2(2p) + 6(2p)
#   0(20p) + 1(10p) + 0(5p) + 1(2p) + 8(2p)
#   0(20p) + 1(10p) + 0(5p) + 0(2p) + 10(2p)
#           Recurse?
#   0(20p) + 0(10p) + 4(5p) + 0(2p) + 0(2p)
#   0(20p) + 0(10p) + 3(5p) + 2(2p) + 1(2p)
#   0(20p) + 0(10p) + 3(5p) + 1(2p) + 3(2p)
#   0(20p) + 0(10p) + 3(5p) + 0(2p) + 5(2p)
#   0(20p) + 0(10p) + 2(5p) + 5(2p) + 0(2p)
#   0(20p) + 0(10p) + 2(5p) + 4(2p) + 2(2p)
#   0(20p) + 0(10p) + 2(5p) + 3(2p) + 4(2p)
#   0(20p) + 0(10p) + 2(5p) + 2(2p) + 6(2p)
#   0(20p) + 0(10p) + 2(5p) + 1(2p) + 8(2p)
#   0(20p) + 0(10p) + 2(5p) + 0(2p) + 10(2p)
#   0(20p) + 0(10p) + 1(5p) + 7(2p) + 1(2p)
#   0(20p) + 0(10p) + 1(5p) + 6(2p) + 3(2p)
#   0(20p) + 0(10p) + 1(5p) + 5(2p) + 5(2p)
#   0(20p) + 0(10p) + 1(5p) + 4(2p) + 7(2p)
#   0(20p) + 0(10p) + 1(5p) + 3(2p) + 9(2p)
#   0(20p) + 0(10p) + 1(5p) + 2(2p) + 11(2p)
#   0(20p) + 0(10p) + 1(5p) + 1(2p) + 13(2p)
#   0(20p) + 0(10p) + 1(5p) + 0(2p) + 15(2p)
#           Recurse
#   0(20p) + 0(10p) + 0(5p) + 10(2p) + 0(2p)
#   0(20p) + 0(10p) + 0(5p) + 9(2p) + 2(2p)
#   0(20p) + 0(10p) + 0(5p) + 8(2p) + 4(2p)
#   0(20p) + 0(10p) + 0(5p) + 7(2p) + 6(2p)
#   0(20p) + 0(10p) + 0(5p) + 6(2p) + 8(2p)
#   0(20p) + 0(10p) + 0(5p) + 5(2p) + 10(2p)
#   0(20p) + 0(10p) + 0(5p) + 4(2p) + 12(2p)
#   0(20p) + 0(10p) + 0(5p) + 3(2p) + 14(2p)
#   0(20p) + 0(10p) + 0(5p) + 2(2p) + 16(2p)
#   0(20p) + 0(10p) + 0(5p) + 1(2p) + 18(2p)
#           Recurse
#   0(20p) + 0(10p) + 0(5p) + 0(2p) + 20(2p)

# determines the biggest coin needed to break the amount
# returns a list of coins that can be used to break 'amount'
def maxCoin(amount, printMax = False):
    coins = [200,100,50,20,10,5,2,1]
    temp = []
    maxCoin = 0
    for i in coins:
        if amount >= i:
            maxCoin = i
            break
    if printMax:
        print(maxCoin) 
    for i  in coins:
        if i <= maxCoin:
            temp.append(i)
    if printMax:
        print(temp)
    return temp

# 2 way to break down 2p
#   1(2p) + 0(1p)
#   Recurse?
#   0(2p) + 2(1p)


# 4 ways to break down 5p
#   1(5p) + 0(2p) + 0(1p)
#   Recurse?
#   2(2p) + 1(1p)
#   1(2p) + 3(1p)
#   Recurse?
#   5(1p)

#   start at Max coin, exhaust all options then decrease. Once max coin is less than 0, return

# cnt = how many of that coin there are
# coin = the coin value
def formatCoin(cnt, coin):
    return ("%d(%dp)" % (cnt, coin))


# EXAMPLE
# amount = 5
# [5, 2, 1]

# returns list of all possible ways to break amount in this format:
    # [1(5p), 2(2p) + 1(1p), ...]
def coinSums(amount, coins, current = 0, ret = []):
    currentCoin = coins[0]
    cnt = 0
    while current < amount:
        cnt += 1
        current+=currentCoin
    if current == amount:
        # if we have reached the amount then add our current place in the list
        ret.append(formatCoin(cnt, coins[0]))
    coinSums(amount, coins[1:0], current, ret)
    print(ret)


# amount is the amount to break
# coins is a list of all coins elligible to use
# current tracks the value of coins of a certain combination
"""
def coinSums(amount, coins, current = 0):
    # if we are at 1p, just fill up to the amount
    if len(coins) == 1:
        return amount - amount
    maxVal = coins[0]
    for i in range(int(amount/maxVal), -1 , -1):
        print(coins[i])
    return coinSums(amount, coins[1:])
    """
        
        
while True:
    # start clock
    start = clock()

    coin = int(input("Enter value to break: "))
    coins = maxCoin(coin)
    print(coinSums(coin, coins))

    # stop clock
    end = clock()
    print("The program took %f seconds to run" % (end - start))
