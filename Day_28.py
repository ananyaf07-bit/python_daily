import time

def simple_decorator(function):
    def wrapper(*args, **kwargs):
        print("Function started")
        result=function(*args, **kwargs)
        print("Function finished")
        return result
    return wrapper

def simple_decorator2(function):
    def wrapper(*args, **kwargs):
        result=function(*args, **kwargs)
        return result
    return wrapper

def timer(function):
    def wrapper(*args, **kwargs):

        start=time.time()
        result=function(*args, **kwargs)
        end=time.time()

        elapsed=end-start
        print("Excecution time:",elapsed,"seconds")

        return result
    return wrapper

def check_positive(function):
    def wrapper(*args, **kwargs):
        if(args[0]>0):
            result=function(*args, **kwargs)
            return result
        else:
            print("Number must be positive")
    return wrapper
    
@simple_decorator
def hello():
    print("Hello,Python!")
hello()

@simple_decorator2
def add(a,b):
    return a+b
op=add(10,20)
print("Sum =",op)

@simple_decorator
def multiply(a,b):
    return a*b
mul=multiply(10,5)
print("Multiply =",mul)

@timer
def calculate():
    total = 0

    for i in range(1, 1000000):
        total += i

    return total
print(calculate())

@check_positive
def calculate_square(n):
    return n * n
sq=calculate_square(-5)
print("Square =",sq)