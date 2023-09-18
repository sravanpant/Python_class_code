string = input("Enter a string: ")
character = []
for i in string:
    if i not in character:
        character.append(i)
        print(f"{i}: {string.count(i)}")
