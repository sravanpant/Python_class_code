import csv

with open("file1.csv", "w", newline="") as file:
    writefile = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    mylist = [["abc", 1], ["def", 2], ["xyz", 3], ["hij", 4]]
    writefile.writerows(mylist)

with open("file1.csv") as file:
    readfile = csv.reader(file)
    for r in readfile:
        print(r)
# with open("file1.csv", "r") as file:
#     readfile = csv.reader(file)
#     for r in readfile:
#         print(r)
