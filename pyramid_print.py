num = int(input("Enter the number: "))
n = num
m = n - 2
size = 5 * n
print(f"              M={m},N={n}")
for i in range(1, n * 2, 2):
    print(" " * size, end="")
    print(f"  {m}  " * i)
    size -= 5
