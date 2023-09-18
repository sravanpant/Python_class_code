name = input("Enter your first name: ")
name = name.lower()

if len(name) % 2 == 0:
    print("Expected Output: " + name[0] + name[len(name) // 2] + name[-1])
else:
    print("Expected Output: " + name[0] + name[(len(name) - 1) // 2] + name[-1])
