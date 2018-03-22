# The Fibonacci sequence is defined by the recurrence relation:
# 
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# I got my sqrt equation from this website (which got it from wolfram)
# https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence

from math import sqrt
def fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)) 
"""
numbers = [1,1]

def fib(num):
    global numbers
    if num == 1:
        return 1
    elif num == 2:
        return 1
    try:
        numbers.append(numbers[num-1] + numbers[num-2])
    except:
        numbers.append(fib(num-1) + fib(num-2))
    return numbers[len(numbers)-1]
    """

def load():
    file = open("outfile.txt","w")
    for i in range(1, 100):
        val = fib(i)
        print(val)
        file.write(str(val)+"\n")
    file.close()
#print(str(fib(int(input("Insert Number: ")))))
load()
print(str(fib(2000)))
