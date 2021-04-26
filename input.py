'''class student():

    def stu1(self, name, familydetails, education, hobies): 
        self.name = name
        self.familydetails = familydetails
        self.education = education
        self.hobies = hobies
        return 

    def display(self, name, familydetails, education, hobies):
        return student()


stud = student()

a = str(input("Enter the name of student: "))
b = str(input("Enter the familydetails of student: "))
c = str(input("Enter the education of student: "))
d = str(input("Enter the hobbies of student: "))

s1 = stud.display(a, b, c, d)
print("The Student Information is: ",s1)
'''

class teacher():

    def stu1(self, name, familydetails, education, hobies):
        self.name = name
        self.familydetails = familydetails
        self.education = education
        self.hobies = hobies
        return self.name, self.familydetails, self.education, self.hobies

    def display(self):
        return student

stud = student()

a = str(input("Enter the name of student: "))
b = str(input("Enter the familydetails of student: "))
c = str(input("Enter the education of student: "))
d = str(input("Enter the hobbies of student: "))

s1 = stud.stu1(a, b, c, d)
print("The Student Information is: ",s1)
