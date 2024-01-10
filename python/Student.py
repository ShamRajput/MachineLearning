class Student:

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def print(self):
        print(self.name)
        print(str(self.rollno))
        print(str(self.marks))
