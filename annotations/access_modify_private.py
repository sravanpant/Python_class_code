class C:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def get_x(self):
        return self.__x

    def set_x(self, a):
        self.__x = a

    def get_y(self):
        return self.__y

    def set_y(self, b):
        self.__y = b


O2 = C()
O2.set_x(45)
O2.set_y(20)
print(O2.get_x(), O2.get_y())
