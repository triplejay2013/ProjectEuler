#http://radiusofcircle.blogspot.com

#time module for execution time
import time

#time at the start of program
start = time.time()

#list to store the fibonacci numbers
# added first two numbers of the 
#fibonacci sequence
fib = [0,1]

#iterator
i = 2

#An infinite loop, breaks 
#when the number is 1000 digits long
while True:
    #using the function given in question
    fib_new = fib[i-1]+fib[i-2]
    #Appending the new fibonacci to the list
    fib.append(fib_new)
    #condition to check for 1000 digits
    if fib_new>10**999:
        print(i)
        break
    i = i+1

#time at the end of execution
end = time.time()

#printing the total time for execution
print(end-start)
