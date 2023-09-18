str1 = input("Enter a string: ")

if len(str1) % 2 == 0:
    print(
        "Expected Output: "
        + str1[len(str1) // 2 - 1]
        + str1[len(str1) // 2]
        + str1[len(str1) // 2 + 1]
    )
else:
    print(
        "Expected Output: "
        + str1[(len(str1) - 1) // 2 - 1]
        + str1[(len(str1) - 1) // 2]
        + str1[(len(str1) - 1) // 2 + 1]
    )
