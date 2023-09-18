n = int(input("Enter the number: "))
sum = 0
while n != 0:
    sum += n % 10
    n = n // 10
print(f"Sum of digits: {sum}")
