# Pentagonal numbers are generated by the formula, P(n)=n(3n−1)/2. The first ten
# pentagonal numbers are:
# 
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# 
# It can be seen that P(4) + P(7) = 22 + 70 = 92 = P(8). However, their difference, 70
# − 22 = 48, is not pentagonal.
# 
# Find the pair of pentagonal numbers, P(j) and P(k), for which their sum and
# difference are pentagonal and D = |P(k) − P(j)| is minimised; what is the value of
# D?
from time import *

def pentagonNum(n):
  return int((n*(3*n - 1))/2)

def isPent(n):
  

while True:
  limit = int(input("Enter how many pentagonal numbers to generate: "))
  start = clock()
  pent = [pentagonNum(i) for i in range(1, limit+1)]
  print(pent)
  special = []
  for i in pent:
    for j in pent:
      if j >= i: continue
      if i+j in pent and i-j in pent:
        special.append([i,j])
  print(special)

  end = clock()
  print("The program took {} seconds to run".format(end-start))
