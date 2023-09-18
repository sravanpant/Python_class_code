num = int(input("Enter the number: "))
reverse_num = 0
while num != 0:
    reverse_num = reverse_num * 10 + (num % 10)
    num = num // 10
print(f"The reversed number: {reverse_num}")
