import math

num = int(input("Enter the number: "))
print(f"The Prime Factors of {num} are: ", end="")
while num % 2 == 0:
    print(2, end=" ")
    num = num / 2

for i in range(3, int(math.sqrt(num)) + 1, 2):
    while num % i == 0:
        print(i, end=" ")
        num = num / i
if num > 2:
    print(num)
print()
