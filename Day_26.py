from functools import reduce
marks = [45, 78, 92, 33, 67, 88, 25, 95]

square=lambda a:a*a
print(square(5))

doubled=list(map(lambda a:a*2,marks))
print(doubled)

passed=list(filter(lambda m:m>=40 ,marks))
print(passed)

total=reduce(lambda a,b:a+b,marks)
print(total)

pass_squares=list((map(lambda a:a*a,filter(lambda a:a>=40,marks))))
print(pass_squares)