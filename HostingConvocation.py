from Convocation import register, getByProgramme, getStudentByRegno


def main():
    registerDetail = []
    choice1 = input(
        "Do you want to register as a graduand for the convocation? (yes/no): "
    )
    if choice1 == "yes":
        detail = []
        detail = register(detail)
        registerDetail.append(detail)
    else:
        pass
    choice2 = input("Do you want to view Program wise Graduands list? (yes/no): ")
    if choice2 == "yes":
        programme = input("Enter the programme to filter the students accordingly: ")
        graduands_list = getByProgramme(registerDetail, programme)
        print(graduands_list)
    else:
        pass
    choice3 = input("Do you want to view a Graduand? (yes/no): ")
    if choice3 == "yes":
        regno = int(
            input("Enter the registration number of the graduand you want to view: ")
        )
        graduand = getStudentByRegno(registerDetail, regno)
        print(graduand)
    print("Programming exiting with exit code 0 ....")


if __name__ == "__main__":
    main()
