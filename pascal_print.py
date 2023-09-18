from math import factorial

num = int(input("Enter the number: "))
for i in range(num):
    for j in range(num - i + 1):
        print(end="  ")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end="   ")
    print()
