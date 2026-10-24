m1=int(input("Enter marks for subject 1:"))
m2=int(input("Enter marks for subject 2:"))
m3=int(input("Enter marks for subject 3:"))
m4=int(input("Enter marks for subject 4:"))
m5=int(input("Enter marks for subject 5:"))
marks=[m1,m2,m3,m4,m5]
count=0
print("Marks:",marks)
for i in marks:
    if(i>=40):
        count+=1
print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Total:",sum(marks))
print("Average:",sum(marks)/len(marks))
print("Subjects passed:",count)
print(marks[::-1])    
