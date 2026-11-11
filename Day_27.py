numbers = [10, 20, 30, 40, 50]
iterator=iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

def even_numbers(n):
    for x in range(2, n + 1):
        if x % 2 == 0:
            yield x

print("\nEven Numbers:\n")
for number in even_numbers(10):
    print(number)

def sqaure_numbers(n):
    for x in range(1, n + 1):
        yield x * x

print("\nSquare Numbers:\n")
for x in sqaure_numbers(5):
    print(x)

def cube_numbers(n):
    for x in range(1, n + 1):
        yield x * x * x

print("\nCube Numbers:\n")
for x in cube_numbers(10):
    print(x)





