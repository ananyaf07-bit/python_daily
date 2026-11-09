students = {"Ananya": 95,"Bhavya": 78,"Sahil": 52,"Rohan": 35,"Neha": 88}

doubled={name:marks*2 for name,marks in students.items()}
print("Doubled:",doubled)

passing={name:marks for name,marks in students.items() if marks>=40}
print("Passing:",passing)

result={name:"Pass" if marks>=40 else "Fail" for name,marks in students.items()}
print("Result:",result)

grade= {name:"A" if m>=90 else "B" if m>=75 else "C" if m>=60 else "D" if m>=40 else "F" for name,m in students.items()}
print("Grade:", grade)