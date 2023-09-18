num = int(input("Enter the number: "))
original_num = num
reverse_num = 0
count = 0
while num != 0:
    reverse_num = reverse_num * 10 + (num % 10)
    num = num // 10
if reverse_num == original_num:
    print(f"{original_num} is a palindrome number.")
else:
    print(f"{original_num} is not a palindrome number.")
