import random

# Generator random numbers
number1 = random.randint(0,20)
number2 = random.randint(10,20)

# prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " + str(number2) + "?"))

# Display result
print (number1, "+" , number2, "=", answer , " is ",number1 + number2 == answer)

x=1
y=1
z=1
maximum = 0
if ( y <= x >= z):
    maximum = x
elif (x <= y >= z ):
    maximum = y
elif (x <= z >= y):
    maximum = z

print(maximum)      

even = False
if even: 
    print("It is even!")