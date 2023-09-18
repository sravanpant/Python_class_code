binary = int(input("Enter the binary number: "))
decimal, i = 0, 0
while binary != 0:
    decimal = decimal + (binary % 10) * (2**i)
    binary = binary // 10
    i += 1
print(f"The number in decimal: {decimal}")
