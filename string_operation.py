# 1. Create a string object and perform the following operations:
# a) create a new string containing first 3 and the last 3 characters
# b) create a new string containing the middle ‘n’ characters
# c) insert a new string in the middle at the given position
# d) rearrange the characters, so that uppercase letters are followed by
# lowercase letters
# e) find the frequency of a substring in the above string
# d) print the characters in reverse order
string = input("Enter a string: ")
n = int(input("Enter a number: "))
string1 = string[0:3] + string[-3:]
print(f"New string containing first 3 and last 3 characters: {string1}")
string2 = ""
for i in range(n):
    string2 += string[(len(string) // 2) - i]
string2 = string2[::-1]
print(f"New string containing the middle {n} characters: {string2}")
string3 = string[0 : len(string) // 2] + string1 + string[len(string) // 2 :]
print(f"New string inserted in the middle: {string3}")
string4 = []
for i in range(len(string)):
    string4.append(string[i])

string4.sort()
string4 = "".join(string4)
print(f"Rearranging the order of string: {string4}")
print("Frequency of substring of the above input string: ")
character = []
for i in string:
    if i not in character:
        character.append(i)
        print(f"{i}: {string.count(i)}")

string5 = string[::-1]
print(f"The characters in reverse order: {string5}")

# 2. Write a program to print the current number, its previous number and the sum of
# these two numbers, in a given range.
