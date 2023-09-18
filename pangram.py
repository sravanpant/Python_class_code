# def isPangram(s):
#     s = s.lower()
#     return all([c in s for c in "abcdefghijklmnopqrstuvwxyz"])

s = input("Enter a sentence: ")


def isPangram(s):
    s = s.lower()
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in s:
            return False
    return True


if isPangram(s):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
