import csv
import json

person_info_list = [
    ["Name", "Status", "Income", "FD_List", "Asset_Value_Dict"],
    [
        "AAA",
        "Professional",
        800000,
        [1200000, 45000, 300000, 200000],
        {"House": 4500000, "Car": 600000, "Land": 4000000, "Jewels": 1000000},
    ],
    [
        "BBB",
        "Politician",
        10000000,
        [2000000, 1000000, 25000000],
        {"House": 30000000, "Car": 2000000, "Land": 100000000, "Jewels": 25000000},
    ],
    [
        "CCC",
        "Employee",
        700000,
        [500000, 20000000, 150000],
        {"House": 1000000, "Jewels": 250000},
    ],
]


with open("person_info.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(person_info_list)


class Person:
    def __init__(self, name, status, income, total_deposits_value, total_assets_value):
        self.name = name
        self.status = status
        self.income = income
        self.total_deposits_value = total_deposits_value
        self.total_assets_value = total_assets_value

    def __str__(self):
        return f"{self.name}, {self.status}, {self.income}, {self.total_deposits_value}, {self.total_assets_value}"

    def validate(self):
        if self.status == "Professional" and (
            self.total_deposits_value > 10 * self.income
            or self.total_assets_value > 25 * self.income
        ):
            raise ValueError("IT Raid Alert")
        elif (
            self.status == "Politician"
            and (self.total_deposits_value + self.total_assets_value) > 10 * self.income
        ):
            raise ValueError("Disproportionate Assets Alert")
        elif (
            self.status == "Employee"
            and (self.total_deposits_value or self.total_assets_value)
            > 20 * self.income
        ):
            raise ValueError("Scam Alert")
        else:
            return "Valid Candidate"


def string_list_to_sum(string):
    string = string[1:-1]
    string = string.split(",")
    string = map(int, string)
    return sum(string)


def string_dict_to_sum(string):
    string = string.replace("'", '"')
    string = json.loads(string)
    value = string.values()
    return sum(value)


with open("person_info.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            deposit_sum = string_list_to_sum(row[3])
            asset_sum = string_dict_to_sum(row[4])
            person = Person(row[0], row[1], int(row[2]), deposit_sum, asset_sum)
            print(person)
            print(person.validate())
        except ValueError as msg:
            print(msg)
