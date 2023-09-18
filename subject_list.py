subject = []
count = 1
while count <= 3:
    row = []
    sub = input("Enter course name: ")
    code = int(input("Enter course code: "))
    credit = int(input("Enter course credit: "))
    row.append(sub)
    row.append(code)
    row.append(credit)
    subject.append(row)
    count += 1
    option = input("Do you want to delete a course? [yes/no] ")
    if option == "yes":
        delete_option = input(
            "Please choose to input either course name or course code: [name/code] "
        )
        if delete_option == "name":
            name = input("Enter the name of the course you want to delete: ")
            for i in range(len(subject)):
                if name == subject[i][0]:
                    subject.remove(subject[i])
                    print("The course named", name, "was successfully removed.")
                    count -= 1
        elif delete_option == "code":
            code = int(input("Enter the code of the course you want to delete: "))
            for i in range(len(subject)):
                if code == subject[i][1]:
                    subject.remove(subject[i])
                    print("The course coded", code, "was successfully removed.")
                    count -= 1
        else:
            print("Invalid value")
            continue
    elif option == "no":
        pass
    else:
        print("Invalid value, opting to value 'no' as default")
        pass

for i in range(len(subject)):
    print(subject[i])

print("Checking for duplicate courses...")
for i in range(len(subject)):
    for j in range(i + 1, len(subject)):
        if subject[i][0] == subject[j][0]:
            print("Duplicate course name:", subject[i][0])
        elif subject[i][1] == subject[j][1]:
            print("Duplicate course code:", subject[i][1])
        else:
            print("No duplicate courses found.")
            pass
