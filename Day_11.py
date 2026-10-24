#DAY 11 Duplicate Remover
num=[]
for i in range(1,6):
    n=int(input("Enter number"))
    num.append(n)
num_set=set(num)  
print("Original list:",num)
print("Unique list:",num_set)
print("Number of unique values:",len(num_set))
print("Sorted unique values:",sorted(num_set))
