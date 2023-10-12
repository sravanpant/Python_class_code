class python:
    def __init__(self, section, regno, rollno):
        self.section = section
        self.regno = regno
        self.rollno = rollno

    def __str__(self):
        return f"{self.section}, {self.regno}, {self.rollno}"


c1 = python("A", 112233, 34)
print(c1)
