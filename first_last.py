string = input("Enter a string: ")

if len(string) < 2:
    string1 = []
else:
    string1 = [string[0], string[1], string[-2], string[-1]]
print("Expected Output: " + "".join(string1))
