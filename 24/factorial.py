def factorial(num):
  if num == 0:
    return 1
  elif num < 0:
    return 0
  ret = 1
  for i in range(2,num+1):
    ret *= i
  return ret

def run():
    done = False
    while done == False:
        num = int(input("Input Number: "))
        if num <= 0:
            done = True
        else:
            print("The factorial of " + str(num) + " is " + str(factorial(num)))
