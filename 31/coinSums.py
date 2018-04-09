# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 
#   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#   How many different ways can £2 be made using any number of coins?
from time import *

coins = [1,2,5,10,20,50,100,200]

def prettyPrint():
  return 0

def coinSums(amount):
  wallet = []
  total = 0
  for i in coins:
    while total < amount:
    

  return wallet

while True:
  # start clock
  start = clock()

  coin = int(input("Enter value to break: "))
  print(coinSums(coin))

  # stop clock
  end = clock()
  print("The program took %f seconds to run" % (end - start))
