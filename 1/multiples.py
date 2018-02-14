# finds all multiples of a given number and finds their sum
# 
# Parameters: 
#	factor1 is the first factor (ex:3)
#	factor2 is the second factor (ex:5)
#	limit is the limit of numbers we will consider (ex:10)
#
# Return: 
#	sum of all factors below the limit
def multipleSum(factor1, factor2, limit):
    sum = 0
    for i in range(1,limit):
        if i%factor1 == 0 or i%factor2 == 0:
            sum+=i
    return sum
            

#print and call multipleSum()
print("multipleSum(3,5,10)", multipleSum(3,5,10))
print("multipleSum(3,5,1000)", multipleSum(3,5,1000))
