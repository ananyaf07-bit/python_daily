marks=[45,78,92,33,67,88,25,95]

doubled=[m*2 for m in marks]
print(doubled)

passed=[m for m in marks if m>=40]
print(passed)

failed=[m for m in marks if m<40]
print(failed)

grade= [ "A" if m>=90 else "B" if m>=75 else "C" if m>=60 else "D" if m>=40 else "F" for m in marks ]
print(grade)

names=["ananya","raj","bhavya","sam","rohan"]

uppercase_names=[name.upper() for name in names]
print(uppercase_names)

long_names=[name for name in names if len(name)>=5]
print(long_names)