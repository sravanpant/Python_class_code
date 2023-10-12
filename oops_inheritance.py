# Parent class
class inherit:
    # inherit is not a keyword
    def __init__(self, secA, secB):
        self.section1 = secA
        self.section2 = secB

    def sections(self):
        print(self.section1, self.section2)


A1 = inherit("Asec", "Bsec")
A1.sections()


# child class -> send the parent class as a parameter when creating a child class
class python(inherit):
    def __init__(self, secA, secB, cia2):
        super().__init__(secA, secB)
        self.cia2 = cia2

    # pass
    # pass when no property/method are added to the class
    # child class python will inherit all the methods and properties from the
    # parent class inherit


A2 = python("C", "D", 161023)
A2.sections()
print(A2.cia2)
