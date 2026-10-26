name=input("Enter name")
age=int(input("Enter age"))
course=input("Enter course")
m1=int(input("Python"))
m2=int(input("Java"))
m3=int(input("Maths"))
student={"name": name,"age": age,"course":course,"marks":{"Python":m1,"Java":m2,"Maths":m3}}
avg=sum(student["marks"].values()) / len(student["marks"])
print("Average marks=",avg)
for i,j in student.items():
    print(i,":",j)