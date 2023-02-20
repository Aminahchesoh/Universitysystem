class User:
    def __init__(self, name, id, phonenum):
        self.name= name
        self.id= id
        self.phonenum= phonenum
    def show_details(self):
        print(f"Student name is {self.name}")
        print(f"Student ID is {self.id}")
        print(f"student phone number is {self.phonenum}")

class Student(User):          #create a class called student and inherit property and method from user class
    def __init__(self, name, id, phonenum, grade, email, major):
        self.grade= grade
        self.email= email
        self.major= major
        User.__init__(self, name, id, phonenum)
        
        User.show_details(self) #this is the first call for show_detail() method
        print(f"{self.name} got {self.grade}") #this print studentName got studentGrade
    # add method to view a subject's marks


class Lecturer(User):
    def __init__(self, name, position, id, building, phonenum, salary):
        self.posiition= position
        self.building= building
        self.salary= salary
        User.__init__(self, name, id, phonenum)
     # add method to set a students mark
    def set_student_marks(self, student, subject, new_grade):
        student.set_marks(subject, new_grade)
        self.students[student.name] = student.grade
        print(f"{self.name} has set {student.name}'s marks for {subject} to {student.grade}")
    def view_student_marks(self, student):
        print(f"{student.name}'s marks are: {self.students[student.name]}")

class Staff(User):
    def __init__(self, name, position, id, building, phonenum, salary):
        self.posiition= position
        self.building= building
        self.salary= salary
        User.__init__(self, name, id, phonenum)


s = Student("Aminah", 642437001, '09878867', "A+", "ugh@ftu.ac.th", "DS")
#s.show_details() #this is the second call for show_detail() method
