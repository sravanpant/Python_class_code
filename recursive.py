def GCD(n, m):
    r = min(n, m)
    while r > 0:
        if n % r == 0 and m % r == 0:
            break
        r -= 1
    return f"GCD of {n} and {m}: {r}"


def factorial(num):
    factorial = 1
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    elif num == 0:
        print("Factorial of 0 is 1.")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        return f"The factorial of {num}: {factorial}"


def Reversing(num):
    reverse_num = 0
    while num != 0:
        reverse_num = reverse_num * 10 + (num % 10)
        num = num // 10
    return f"The reversed number: {reverse_num}"


print(GCD(30, 20))
# print(factorial(5))
# print(Reversing(1234))
