num = int(input("Enter the number: "))
sum = 0
n = 1
if num < 0:
    print("Invalid input.")
elif num == 0:
    print("Invalid input.")
else:
    while n <= num:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
        sum += 1 / factorial
        n = n + 1

    if num == 1:
        print(f"The sum of 1/1! = {sum}")
    else:
        print("The sum of ", end="")
        for i in range(1, num + 1):
            if i == num:
                print(f"1/{i}! ", end="")
            else:
                print(f"1/{i}! + ", end="")
        print(f"= {sum:.2f}")
