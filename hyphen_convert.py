string = input("Input String: ")
string = string.split("-")

string.sort()

string = "-".join(string)
print("Output: " + string)
