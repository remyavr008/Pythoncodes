class Student:
    schoolname="abcschool2"
    def __init__(self,name,age): #self is a keyword that is used to point a specific object
        print("This is a constructor")
        self.name=name #instance variable
        self.age=age #instance variables
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("schoolname ",Student.schoolname)
#object creation
student1=Student("Remya",35)
student1.display()
student2=Student("newname",26)
student2.display()
