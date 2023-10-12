def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


try:
    n = int(input("Enter a number: "))
    if n < 0:
        raise ValueError("Negative number")
    elif n > 20:
        raise ValueError("Number greater than 20")
    else:
        for i in range(n + 1):
            print(fibo(i), end=" ")
        print()
except ValueError as e:
    print(e)
