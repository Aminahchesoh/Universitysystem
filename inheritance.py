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
    def __init__(self, name, id, phonenum, marks, email, major):
        self.marks= marks
        self.email= email
        self.major= major
        User.__init__(self, name, id, phonenum)
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def view_marks(self, subject):
        if subject in self.marks:
            print(f"{self.name}'s marks for {subject}: {self.marks[subject]}")
        else:
            print(f"{self.name} has not received any marks for {subject} yet.")
        
        User.show_details(self) #this is the first call for show_detail() method
        print(f"{self.name} got {self.marks}") #this print studentName got studentGrade
    # add method to view a subject's marks (miniProjectMark, finalProjectMark, attendance mark, exersicesDiscussionMark)


class Lecturer(User):
    def __init__(self, name, position, id, building, phonenum, salary):
        self.posiition= position
        self.building= building
        self.salary= salary
        User.__init__(self, name, id, phonenum)

    # add method to set a students mark (miniProjectMark, finalProjectMark, attendance mark, exersicesDiscussionMark)
    def set_studentmark (self, miniProjectMark, finalProjectMark, attendancemark,exersicesDiscussionMark):
        self.studentmark = miniProjectMark
        self.studentmark = finalProjectMark
        self.studentmark = attendancemark
        self.studentmark = exersicesDiscussionMark
        print(f"{self.name} has set {Student.name}'s marks {Student.mi}  {Student.grade}")

        



class Staff(User):
    def __init__(self, name, position, id, building, phonenum, salary):
        self.posiition= position
        self.building= building
        self.salary= salary
        User.__init__(self, name, id, phonenum)
#create course class to link it with Students & Lecturer classes using composition later
class Course:
    def __init__(self, cName, cId, cMidterm, cMiniProject, cFinalProject, cFinalExam, cDiscussion):
        self.name = cName
        self.id = cId
        self.midterm = cMidterm
        self.miniProject = cMiniProject
        self.finalProject = cFinalProject
        self.finalExam = cFinalExam
        self.discussions = cDiscussion
        

s = Student("Aminah", 642437001, '09878867', "A+", "ugh@ftu.ac.th", "DS")
# create an object of exersicesDiscussionMark class
discussMark = exersicesDiscussionMark("Theory class", 20)
discussMark.show_details()
#s.show_details() #this is the second call for show_detail() method
""" for future use
# Code to demonstrate Aggregation

# Salary class with the public method
# annual_salary()
class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def annual_salary(self):
		return (self.pay*12)+self.bonus


# EmployeeOne class with public method
# total_sal()
class EmployeeOne:

	# Here the salary parameter reflects
	# upon the object of Salary class we
	# will pass as parameter later
	def __init__(self, name, age, sal):
		self.name = name
		self.age = age

		# initializing the sal parameter
		self.agg_salary = sal # Aggregation

	def total_sal(self):
		return self.agg_salary.annual_salary()

# Here we are creating an object
# of the Salary class
# in which we are passing the
# required parameters
salary = Salary(10000, 1500)

# Now we are passing the same
# salary object we created
# earlier as a parameter to
# EmployeeOne class
emp = EmployeeOne('Geek', 25, salary)

print(emp.total_sal())


"""
