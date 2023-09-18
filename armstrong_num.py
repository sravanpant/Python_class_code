n = int(input("Enter the number: "))
m = n
sum = 0
count = 0
while m != 0:
    m = m // 10
    count += 1
m = n
while m != 0:
    sum += (m % 10) ** count
    m = m // 10

if sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
