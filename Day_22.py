import json

students=[{"Name":"Ananya","roll_no":3579,"course":"Btech","marks":95},
{"Name":"Bhavya","roll_no":2558,"course":"BDS","marks":85},
{"Name":"Sahil","roll_no":8975,"course":"Btech","marks":52}]


with open("students.json","w") as file:
    json.dump(students,file,indent=4)

with open("students.json","r") as file:
    students=json.load(file)
    print("\n---STUDENT DATABASE---\n")
    for student in students:
        print("Name:",student["Name"])
        print("Roll No:",student["roll_no"])
        print("Course:",student["course"])
        print("Marks:",student["marks"],"\n")

    roll_search=int(input("Enter roll number to search:"))
    flag=0
    for student in students:
        if student["roll_no"]==roll_search:
            print("Student Found")
            print("Name:",student["Name"])
            print("Roll No:",student["roll_no"])
            print("Course:",student["course"])
            print("Marks:",student["marks"],"\n")
            flag=1
    if flag==0:
        print("Student not found")

    roll=int(input("Enter roll number to update:"))
    flag=0
    for student in students:
        if student["roll_no"]==roll:
            update=int(input("Enter new marks:"))
            student["marks"]=update
            flag=1
    if flag==0:
        print("Student not found")

with open("students.json","w") as file:
    json.dump(students,file,indent=4)
    