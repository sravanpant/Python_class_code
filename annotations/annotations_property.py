class A:
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

    x = property(get_x, set_x)
    y = property(get_y, set_y)


O1 = A()


class A:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def get_x(self):
        return self.__x

    def set_x(self, a):
        self.__x = a

    def get_y(self):
        return self.__y

    def set_y(self, b):
        self.__y = b

    x = property(get_x, set_x)
    y = property(get_y, set_y)
