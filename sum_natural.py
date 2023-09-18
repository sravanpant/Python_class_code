n = int(input("Enter the number: "))
sum = 0
for i in range(n):
    sum = sum + (n - i)
print(f"Sum of natural numbers {n}: {sum}")
