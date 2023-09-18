num = int(input("Enter the number: "))
current_num = 1
stop = 2
print("       N =", num)

for i in range(num):
    for j in range(1, stop):
        print(current_num, end=" ")
        current_num += 1
    print()
    stop += 1
