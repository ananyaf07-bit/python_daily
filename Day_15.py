import math as m
import random as rdm

num=int(input("Enter a number"))
if num<0:
    print("Please enter a positive integer")
else:
    print("Square root of the number:",m.sqrt(num))
    print("Factorial of the number:",m.factorial(num))

print("A random integer between 1 and 100:",rdm.randint(1,100))

def square(n):
    return n*n

print("Square:",square(num))