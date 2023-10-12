import csv
from person_info import Person

candidate_list = []


def createCand_list():
    try:
        with open("person_info.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                candidate_list.append(Person(row[0], row[1], int(row[2]), row[3], row))
    except (ValueError, FileNotFoundError) as msg:
        print(msg)
    finally:
        for i in range(len(candidate_list)):
            print(candidate_list[i])


createCand_list()
