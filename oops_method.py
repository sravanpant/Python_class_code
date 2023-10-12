class python:
    def __init__(self, section, rollno):
        self.section = section
        self.rollno = rollno

    def first(self):
        print("my class is " + self.section)


a1 = python("A", 66)
a1.first()
