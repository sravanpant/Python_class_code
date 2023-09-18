n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

r = min(n, m)
while r > 0:
    if n % r == 0 and m % r == 0:
        break
    r -= 1
print(f"GCD of {n} and {m}: {r}")
print(f"LCM of {n} and {m}: {n * m // r}")
