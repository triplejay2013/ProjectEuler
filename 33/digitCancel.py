# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than
# one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.
from time import *

def gcd(a,b):
  if b > a:
    return gcd(b,a)
  if a%b == 0:
    return b
  return gcd(b,a%b)

def reduceFraction(num, den):
  #only considering divisibility for numbers 0-99
  factor = gcd(num,den)
  num = int(num)/factor
  den = int(den)/factor

  return ("%d/%d" % (num,den))

# num(erator), den(ominator)
def digitCancel(num, den):
  num = list(str(num))
  den = list(str(den))
  ret = ""

  for i in num:
    for j in den:
      # if the digits are the same
      if i==j:
        num.remove(i)
        den.remove(j)
        break
  ret = num[0] + "/" + den[0]
  return ret

while True:
  start = clock()

  print(gcd(49,98))
  num = int(input("Enter numerator: "))
  den = int(input("Enter denomenator: "))
  print("Digit Cancelling of %d and %d gives us %s" % (num, den, digitCancel(num, den)))
  print("Reducing the fraction gives us " + reduceFraction(num,den))
  input("Press enter to continue")

  for i in range(10,100):
    for j in range(i+1, 100):
      print(reduceFraction(num,den))
      cancel = digitCancel(num,den)
      # check simplist form of digitcancel
      if reduceFraction(int(cancel[0]), int(cancel[2])) == reduceFraction(num,den):
        print(cancel)
  end = clock()
  print("The program took %f seconds to run" % (end-start))
