class python:
    def __init__(ece, section, regno, rollno):
        ece.section = section
        ece.regno = regno
        ece.rollno = rollno


c1 = python("A", 112233, 55)
print(c1.section)
print(c1.regno)
print(c1.rollno)
