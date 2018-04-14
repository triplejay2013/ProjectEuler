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
  n = list(str(num))
  d = list(str(den))

  done = False
  for i in n:
    for j in d:
      # if the digits are the same
      if i==j:
        n.remove(i)
        d.remove(i)
        done = True
        break
    if done: break
  if done:
    return n[0] + "/" + d[0]
  return ""

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
      if i % 10 == 0 or j % 10 == 0:
        continue
      cancel = digitCancel(i,j)
      if len(cancel) == 0: continue
      if reduceFraction(int(cancel[0]), int(cancel[2])) == reduceFraction(i,j):
        print(str(i)+"/"+ str(j) +" => " + cancel)
  end = clock()
  print("The program took %f seconds to run" % (end-start))
