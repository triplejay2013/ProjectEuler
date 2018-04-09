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
# 3 ways to break down 5p
#   2(2p) + 1(1p)
#   1(2p) + 3(1p)
#   0(2p) + 5(1p)
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
# ways to break down 20p
#   2(10p) + 0(5p) + 0(2p) + 0(2p)
#   1(10p) + 2(5p) + 0(2p) + 0(2p)

#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)
#   0(10p) + 0(5p) + 0(2p) + 0(2p)

def coinSums(amount):
  coins = [200,100,50,20,10,5,2,1]
  i = 0
  while amount - coins[i] < 0:
    i += 1
  # shorten list to remove unnecessary values
  print(coins)
  coins = coins[i+1:]
  print(coins)


while True:
  # start clock
  start = clock()

  coin = int(input("Enter value to break: "))
  print(coinSums(coin))

  # stop clock
  end = clock()
  print("The program took %f seconds to run" % (end - start))
