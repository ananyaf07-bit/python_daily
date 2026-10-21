marks=int(input("Enter your marks"))
if(marks>=0 and marks<101):
    if(marks>=90):
        print("A")
    elif(marks>=75):
        print("B")
    elif(marks>=60):
        print("C")
    elif(marks>=40):
        print("D")
    else:
        print("Fail")
else:
    print("Invalid marks")