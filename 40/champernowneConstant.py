# An irrational decimal fraction is created by concatenating the positive
# integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of the
# following expression.
# 
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

from time import *

while True:
  start = clock()
  limit = int(input("Enter limit (1,000,000): "))
  fraction = ""
  for i in range(1, limit*2):
    fraction += str(i)
  print(fraction)
  print("The 12th fractional part is {}".format(fraction[11]))


  # fractional Parts
  fP = []
  divisor = 1
  print(fraction[:25])
  for i in range(1, limit*2):
    if i%divisor == 0:
      divisor *= 10
      fP.append(fraction[i-1])
      print("The fraction part of {} is {}".format(i,fraction[i-1]))
  

  end = clock()
  print("The Program took {} seconds to run".format(end-start))
