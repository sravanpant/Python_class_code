num = int(input("Enter the number: "))


for i in range(num + 1):
    for j in range(1, num - i + 1):
        print(end="  ")
    for j in range(i, -1, -1):
        print(j, end=" ")
        if j == 0:
            for j in range(1, i + 1):
                print(j, end=" ")

    print()
