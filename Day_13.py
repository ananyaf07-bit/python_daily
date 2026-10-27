students = [
    {"name": "Ananya", "age": 20, "marks": 92},
    {"name": "Riya", "age": 19, "marks": 85},
    {"name": "Aman", "age": 20, "marks": 78}
]

for i in range(0,3):
    print("NAME:",students[i]["name"])
    print("AGE:",students[i]["age"])
    print("MARKS:",students[i]["marks"])

marks = [student["marks"] for student in students]
average = sum(marks) / len(marks)
print("Average",average)
print(max(student["marks"]for student in students))

name=input("Enter name")
age=int(input("Enter age"))
marks=input("Enter marks")
new_student={"name":name,"age":age,"marks":marks}
students.append(new_student)

print("UPDATED LIST:")
for i in range(0,4):
    print(students[i]["name"])
    print(students[i]["age"])
    print(students[i]["marks"])