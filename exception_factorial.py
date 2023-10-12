def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


try:
    n = int(input("Enter a number: "))
    if n < 0:
        raise ValueError("Negative number")
    elif n > 20:
        raise ValueError("Number greater than 20")
    else:
        print(f"Factorial of {n}: {factorial(n)}")
except ValueError as msg:
    print(msg)
