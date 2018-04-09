# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
# 
# 2^2=4, 2^3=8, 2^4=16, 2^5=32
# 3^2=9, 3^3=27, 3^4=81, 3^5=243
# 4^2=16, 4^3=64, 4^4=256, 4^5=1024
# 5^2=25, 5^3=125, 5^4=625, 5^5=3125
# If they are then placed in numerical order, with any repeats removed, we get
# the following sequence of 15 distinct terms:
# 
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
# 
# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and
# 2 ≤ b ≤ 100?

from time import *

def distinctPowers(a,b):
  dP = []
  for i in range(2,a+1):
    for j in range(2, b+1):
      dP.append(pow(i,j))
  # remove duplicates
  dP = list(set(dP))
  # sort the list (for aesthetic purposes)
  dP.sort()
  return dP

while True:
  # start clock
  start = clock()

  a = int(input("Lower Bound: "))
  if a == 0: break
  b = int(input("Upper Bound: "))
  if b < a: break
  dP=distinctPowers(a,b)
  if len(dP) < 50:
    print(dP)
  print(len(dP))

  # stop clock
  end = clock()
  print("The program ran for %f seconds" % (end - start))