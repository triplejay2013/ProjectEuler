"""
Self Powers
Problem 48

The series, 1^1+2^2+3^3+...+10^10 = 10405071317

Find the last ten digits of the series, 1^1+2^2+3^3+...+1000^1000"""

# takes a base to the power of itself. (ie n^n)
def selfPow(n):
    return n**n

x=0
for i in range(1,1001):
    x+=selfPow(i)

print(x)
x=str(x)
print("The last 10 digits are: {}".format(x[len(x)-10:]))
