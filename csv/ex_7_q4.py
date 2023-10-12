import csv

try:
    with open("student_info.csv", "w") as file:
        writefile = csv.writer(file)
        student_info_list = [
            ["Reg No.", "Name", "Maths", "Physics", "Chemistry"],
            [12333, "Rahul", 90, 80, 70],
            [12334, "Utkarsh", 60, 50, 70],
            [12335, "Anuj", 60, 80, 70],
            [12336, "Abhimanyu", 20, 10, 30],
        ]
        writefile.writerows(student_info_list)
    n = len(student_info_list)
    for i in range(1, n):
        avg_marks = (
            student_info_list[i][2] + student_info_list[i][3] + student_info_list[i][4]
        ) / 3
        print(f"Average Marks of {student_info_list[i][1]}: {avg_marks}")
        print(f"Marks in Maths: {student_info_list[i][2]}")
        print(f"Marks in Physics: {student_info_list[i][3]}")
        print(f"Marks in Chemistry: {student_info_list[i][4]}")

except FileNotFoundError:
    print("File does not exists!")


# import csv

# try:
#     with open("D:/125004286/book_info.csv", "w", newline="") as file:
#         writefile = csv.writer(file)
#         book_info_list = [
#             ["Acc No.", "Title", "Author", "Publisher", "Year", "Price"],
#             [
#                 1234,
#                 "Murder on the Orient Express",
#                 "Agatha Christie",
#                 "Random House publications",
#                 2006,
#                 350,
#             ],
#         ]
#         writefile.writerows(book_info_list)
# except FileNotFoundError:
#     print("File does not exists!")
