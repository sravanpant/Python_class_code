n = int(input("Enter the number: "))
print(f"Multiplication table of {n}:")
for i in range(10):
    print(f"{n} x {i+1} = {n*(i+1)}")
