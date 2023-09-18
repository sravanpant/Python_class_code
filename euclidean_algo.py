a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b:
    a, b = b, a % b
print(f"GCD of 2 numbers: {a}")
