# 2) Write a program to print the current number,
# its previous number and the sum of these 2 nums in a given range
num1 = int(input("Enter the first number of a range: "))
num2 = int(input("Enter the last number of a range: "))

for i in range(num1, num2 + 1):
    sum = 0
    print(f"Current number: {i}")
    print(f"Previous number: {i-1}")
    print(f"Sum of the above two numbers: {2 * i - 1}")
