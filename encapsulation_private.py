class A:
    def __init__(self):
        self.__x = 10


A1 = A()
# print(A1.__x) # --> this gives attribute error as it is trying to access private attribute
print(A1._A__x)
