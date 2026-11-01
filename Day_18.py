class Student:
    def __init__(self,name,age,course,marks):
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
        print("Marks:",self.marks)

    def calculate_grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return "B"
        elif self.marks>=60:
            return "C"
        elif self.marks>=40:
            return "D"
        else:
            return "F"

    def is_passed(self):
        if self.marks>=40:
            print("Passed")
        else:
            print("Failed")

s1=Student("Ananya",20,"BTech",98)
s2=Student("Bhavya",20,"BDS",78)

print("---STUDENT 1---\n")
s1.display()
print("Grade:",s1.calculate_grade())
s1.is_passed()


print("\n---STUDENT 2---\n")
s2.display()
print("Grade:",s2.calculate_grade())
s2.is_passed()