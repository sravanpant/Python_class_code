n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
print(f"Prime numbers between {n} and {m} are:")
if n == 1:
    n += 1
while n <= m:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
    n += 1
