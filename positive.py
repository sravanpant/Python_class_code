num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
    num = num * -1
    print(f"Positive number is {num}")
