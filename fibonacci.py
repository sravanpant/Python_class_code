num = int(input("Enter the number: "))


def fib(num):
    n1, n2 = 0, 1
    next_num = n2
    if num == 0:
        print(n1)
    elif num == 1:
        print(n1, n2)
    else:
        print(n1, n2, end=" ")
        for i in range(2, num + 1):
            next_num = n1 + n2
            n1, n2 = n2, next_num
            print(next_num, end=" ")
        print()


fib(num)
