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
    # add method to view a subject's marks (miniProjectMark, finalProjectMark, attendance mark, exersicesDiscussionMark)


class Lecturer(User):
    def __init__(self, name, position, id, building, phonenum, salary):
        self.posiition= position
        self.building= building
        self.salary= salary
        User.__init__(self, name, id, phonenum)
     # add method to set a students mark (miniProjectMark, finalProjectMark, attendance mark, exersicesDiscussionMark)


class Staff(User):
    def __init__(self, name, position, id, building, phonenum, salary):
        self.posiition= position
        self.building= building
        self.salary= salary
        User.__init__(self, name, id, phonenum)
#create course class to link it with Students & Lecturer classes using composition later
class Course:
    def __init__(self, cName, cId, cMidtrm, cMiniProject, cFinalProject, cFinalExam, cDiscussion):
        self.name = cName
        self.id = cId
        self.midterm = cMidterm
        self.miniProject = cMiniProject
        self.finalProject = cFinalProject
        self.finalExam = cFinalExam
        self.discussions = cDiscussuin
        

s = Student("Aminah", 642437001, '09878867', "A+", "ugh@ftu.ac.th", "DS")
#s.show_details() #this is the second call for show_detail() method
