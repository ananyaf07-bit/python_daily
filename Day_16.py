name=input("Enter your name")
age=int(input("Enter age"))
course=input("Enter your course")
current_day=int(input("Enter your currrent python learning day"))

with open("Student_record.txt","w") as f:
    f.write(name+"\n")
    f.write(str(age)+"\n")
    f.write(course+"\n")
with open("Student_record.txt","a") as f:
    f.write(str(current_day)+"\n")
    print("Record saved successfully!")
with open("Student_record.txt","r") as f:
    print("---STUDENT RECORD---")
    n=f.readline()
    a=f.readline()
    c=f.readline()
    cd=f.readline()
    print("Name:",n.strip())
    print("Age:",a.strip())
    print("Course:",c.strip())
    print("Python Learning Day:",cd.strip())





