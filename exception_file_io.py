try:
    file_name = input("Enter the file name: ")
    with open(file_name) as file:
        print()
        print("reading all the contents at once using read()")
        contents = file.read()
        print(contents)

    with open(file_name) as file:
        print()
        print("read all the contents at once using readlines()")
        contents = file.readlines()
        for line in contents:
            print(line, end="")
        print()

    with open(file_name) as file:
        print()
        print("read the contents line by line using readline()")
        line = file.readline()
        while line:
            print(line, end="")
            line = file.readline()
        print()

except FileNotFoundError:
    print(f"File {file_name} not found!!!")
