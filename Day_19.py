class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self,name,age,course,marks):
        super().__init__(name,age)
        self.course=course
        self.marks=marks

    def display(self):
        super().display()
        print("Course:", self.course)
        print("Marks:", self.marks)

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

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Subject:",self.subject)

print("\n---Student 1---")
s1=Student("Ananya",20,"BTech",98)
s1.display()
print("Grade:",s1.calculate_grade())

print("\n---Student 2---")
s2=Student("Bhavya",19,"Vet",78)
s2.display()
print("Grade:",s2.calculate_grade())

print("\n---Teacher---")
t1=Teacher("Vishal Rathee",24,"C")
t1.display()


