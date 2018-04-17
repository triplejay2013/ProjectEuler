# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p ≤ 1000, is the number of solutions maximised

# ANALYSIS
"""
p=120

  |\
48| \52
  |__\
   20
   checked google to find above values
"""
# end analysis


from time import *
from math import *

def perimeter(p=120):
  ret = []
  a = []
  for i in range(1, p+1):
    for j in range(1, p+1):
      if j in a: continue
      if i + j + sqrt(i**2 + j**2) == p:
        a.append(i)
        ret.append([i,j,int(sqrt(i**2 + j**2))])
  return ret


while True:
  limit=int(input("Enter a limit: "))
  start = clock()
  most = -1
  index = -1
  for i in range(1,limit+1):
    p = perimeter(i)
    print("I: {}  with {} solutions".format(i, len(p)))
    if len(p) > most:
      most = len(p)
      index = i
  print("Index {} has the most solutions of {}".format(index,most))
  end = clock()
  print("The program took {} seconds to run".format(end-start))
