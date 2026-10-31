try:
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    op=input(" Enter operator +,-,*,/ ")
except ValueError:
    print("Enter valid numbers and operators")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    if(op=='+'):
        print("Result:",a+b)
    elif(op=='-'):
        print("Result:",a-b)
    elif(op=='*'):
        print("Result:",a*b)
    else:
        print("Result:",a/b)
finally:
    print("Calculator Closed.")