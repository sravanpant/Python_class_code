a = 10


def fn1():
    a = 20

    def fn2():
        a = 30
        print(a)

    fn2()
    print(a)


fn1()
print(a)
