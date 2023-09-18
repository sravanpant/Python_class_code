def main():
    list1 = [123004289, "Rahul Sharma", "123004289@sastra.ac.in", "BTECH", "yes"]
    graduand_list = getByProgramme(list1, "BTECH")
    print(graduand_list)


def register(list1: list):
    regno = int(input("Enter your registration number: "))
    name = input("Enter your name: ")
    email_id = input("Enter your email id: ")
    programme = input("Enter your programme: ")
    choice = input("Enter your willingness to attend convocation? (yes/no): ")
    list1.append(regno)
    list1.append(name)
    list1.append(email_id)
    list1.append(programme)
    list1.append(choice)
    print("Registered Successfully!")
    return list1


def getByProgramme(list1: list, programme):
    list2 = []
    for i in range(len(list1)):
        if list1[i][3] == programme:
            list2.append(list1[i])
    return list2


def getStudentByRegno(list1: list, regno):
    for i in range(len(list1)):
        if list1[i][0] == regno:
            if list1[i][4] == "yes":
                print("Graduand has registered!")
                return list1[i]
            else:
                print("Graduand has not registered!")
                return list1[i]
        else:
            return "Graduand not found!"


if __name__ == "__main__":
    main()
