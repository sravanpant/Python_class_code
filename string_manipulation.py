#  Use for loop construct for the following: accept ‘n’ strings as input. Do the following
# in each string.
# a) reverse the case of each character
# b) remove the vowels and print the new string
# c) remove the duplicate characters in each string and print the new string
# d) compare the current string with the previous string; if they match, print
# ‘Duplicate value’

n = int(input("Enter any number: "))
for i in range(1, n + 1):
    # swaping case
    string = input("Enter any string: ")
    print(string.swapcase())
    # removing vowel
    string1 = []
    for i in range(len(string)):
        if string[i] not in ["a", "e", "i", "o", "u", "A", "I", "O", "U"]:
            string1.append(string[i])
    print("".join(string1))
    # removing duplicate strings
    string2 = string
    for i in string:
        if string.count(i) > 1:
            string = string.replace(i, "")
    print(string)
