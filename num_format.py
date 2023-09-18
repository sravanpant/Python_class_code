num = int(input("Enter the number: "))
n, m = 1, 0
print("       N =", num)
while n <= num:
    for i in range(1, num + 1):
        if i + m < 10:
            print(" ", i + m, " ", end=" ")
        elif i + m >= 10:
            print(" ", i + m, " ", end="")
    print()
    n += 1
    m += num
