# The nth term of the sequence of triangle numbers is given by, t vn = (1/2)*n(n+1); so
# the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t v10. If the word value
# is a triangle number then we shall call the word a triangle word.
# 
# Using words.csv (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?
from time import *

def triangleNum(n):
  return int((1/2)*(n*(n+1)))

def getListFromFile(inputFile):
  outputList = []
  try:
    source = open(inputFile,"r")
    output =  source.readlines()
    outputList = output[0].split(",")
    source.close()
  except FileNotFoundError:
    print("Unable to open input file: " + inputFile)
  return outputList

def triangleWord(word):
  alphabet = ["", "a", "b", "c","d", "e", "f", "g", "h", "i" ,"j"
  ,"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  val = 0
  for i in word:
    if i.lower() in alphabet:
      val += alphabet.index(i.lower())
  return val

while True:
  start = clock()
  limit = int(input("Enter limit: "))
  # test triangle nums
  print("printing triangle numbers up to {}".format(limit))
  # test triangle coded word SKY
  print("testing triangle coded words sky")
  if triangleWord("SKY") == 55: print("YES")
  else: print("NO")
  
  # solve project euler
  print("Uploading File for testing")
  words = getListFromFile("./words.csv")
  triNums = [triangleNum(i) for i in range(1,10000)]
  triWords = []
  for i in words:
    if triangleWord(i) in triNums:
      triWords.append(i)


  print(triWords)
  print("{} of the words are triangles".format(len(triWords)))
  end = clock()
  print("The program took {} seconds to run".format(end-start))
