#STUDENT MANAGEMENT SYSTEM

class Student:
    def __init__(self,name,roll_no,course,marks):
        self.name=name
        self.roll_no=roll_no
        self.course=course
        self.__marks=marks

    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("Course:",self.course)
        print("Marks:",self.__marks)
        print("Grade:",self.calculate_grade())

    def calculate_grade(self):
        if self.__marks>=90:
            return "A"
        elif self.__marks>=75:
            return "B"
        elif self.__marks>=60:
            return "C"
        elif self.__marks>=40:
            return "D"
        else:
            return "F"

    def update_marks(self,update):
        if update>=0 and update<=100:
            self.__marks=update
            print("\nUpdating Marks...\n")
        else:
            print("\nInvalid Marks\n")

    def get_marks(self):
        return self.__marks

s1 = Student("Ananya", 101, "BTech CSE", 95)
s2 = Student("Bhavya", 102, "BDS", 78)

print("\nSTUDENT 1:\n")
s1.display()

print("\nSTUDENT 2:\n")
s2.display()

s2.update_marks(85)
s2.display()

s2.update_marks(150)
s2.display()

class StudentManagement:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)

    def display_all(self):
        for student in self.students:
            student.display()

    def search_student(self,roll_no):
        flag=0
        for student in self.students:
            if(student.roll_no==roll_no):
                student.display()
                flag=1
                break 

        if flag==0:
            print("Student not found")

m = StudentManagement()

m.add_student(s1)
m.add_student(s2)

print("\n--- ALL STUDENTS ---")
m.display_all()

print("\n--- SEARCH STUDENT ---")
m.search_student(102)

print("\n--- SEARCH STUDENT ---")
m.search_student(999)


        


