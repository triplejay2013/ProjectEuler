# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# **21** 22 23 24 **25**
# 20  **7**  8  **9** 10
# 19  6  **1**  2 11
# 18  **5**  4  **3** 12
# **17** 16 15 14 **13**
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# x4 ... x1
# .       .
# .       .
# .       .
# x3 ... x2
#
# n = 0, means a square of one, meaning the center
# all other squares are derived as follows
# x1 = (2n+1)**2 for n > 0
# x2 = (x1 - 6n) for n > 0
# x3 = (x2 + 2n) for n > 0
# x4 = (x3 + 2n) for n > 0
#
# n     1     2     3     4     5     6     7     8     9     10
# (sum is sum of x1 + x2 + x3 + x4)
# sum   1     24    76    160   276   424   604   816   1060    1644
#
#
# sum of spiral diagonals
# n           0     1     2     3     4     5     6     7     8     9
# sum         1     25    101   261   537   961   1565  2381  3441  4777
# first diff        24    76    160   276   424   604   816   1060  1644
# second diff             52    84    116   148   180   212   244   276
# third diff                    32    32    32    32    32    32    32
#
# Therefor we have a closed form of type ax**3 + bx**2 + cx + d
#
# I use the link below to solve for the coefficients
# http://math.bd.psu.edu/~jpp4/finitemath/4x4solver.html
#
#
# Closed Form:
# ((16*x)**3)/3 + (10*x)**2 + (26*x)/3 + 1
#
# a square of width 1001 occurs when n = 500
# from above equations x1-x4 = width = 1001 = 2n + 1
#
# ****note, width will always be odd!****
#
# Therefor: 1001/2 = n = 500

def spiralSquare(n):
  return ((16*(n**3))/3) + (10*(n**2)) + ((26*n)/3) + 1


# EXAMPLE PRINT
#
#   7 8 9 
#   6 1 2 
#   5 4 3

# 21  22  23  24  25
# 20  07  08  09  10
# 19  06  01  02  11
# 18  05  04  03  12
# 17  16  15  14  13

def printSpiral(w):
  n = (w - 1)/2
  def x1(n): return ((2*n)+1)**2
  def x2(n): return x1(n) - 6*n
  def x3(n): return x2(n) + 2*n
  def x4(n): return x3(n) + 2*n

  output = str(int(x4(n))) + "  "
  for i in range(1,w):
    for j in range(1,w):
      output += str(int(x4(n) + j)) + "  "
    output+= "\n" + str(int(x4(n)) - 1) + "  " 
  print(output)


while True:
  n=int(input("Enter Number: "))
  print("Spiral Square of %d is %d" % (n, spiralSquare(n)))
  w=int(input("Enter Width (must be odd!): "))
  if w % 2 == 0:
    w += 1
  printSpiral(w)
