user_input = input("Enter a string: ")

chr_frequency = {string: user_input.count(string) for string in user_input}

print("Output:", chr_frequency)
