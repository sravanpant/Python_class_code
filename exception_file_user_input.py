try:
    with open("userInput.txt", "w") as file:
        pass
    text_input = ""
    with open("userInput.txt", "w") as file:
        print("Enter any text...")
        print("Enter 'End' to end the program")
        while text_input != "End":
            text_input = input("Input: ")
            file.write(text_input + "\n")

    with open("userInput.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File userInput.txt does not exist!!!")
