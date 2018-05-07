print("""
Largest Palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609

""")

from time import clock

def _isPalindrome(word, start, end):
    if start >= end: return True
    if word[start] == word[end]: return _isPalindrome(word, start+1, end-1)
    return False

def isPalindrome(word):
    return _isPalindrome(word, 0, len(word)-1)

while True:
    try:
        limit = int(input("Enter limit (Default 999): "))
    except ValueError:
        limit = 1000
    start = clock()
    myList = [int(i*j) for i in range(int(limit/10),limit) for j in range(i,limit) if isPalindrome(str(i*j))]
    print("The largest palindromic number of numbers less than {} is {}".format(limit, max(myList)))
    print("The program took {} seconds to run".format(clock()-start))
