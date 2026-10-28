def calculate_average(m1,m2,m3):
    return (m1+m2+m3) / 3

def get_grade(average):
    if average>90:
        return "A"
    elif average>75:
        return "B"
    elif average>60:
        return "C"
    elif average>40:
        return "D"
    else:
        return "F"

name=input("Enter your name")
m1=int(input("Enter marks for subject 1:"))
m2=int(input("Enter marks for subject 2:"))
m3=int(input("Enter marks for subject 3:"))


average = calculate_average(m1, m2, m3)
grade = get_grade(average) 

print("Student:",name)
print("Average:",average)
print("Grade:",grade)
