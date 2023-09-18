# fp = open("/home/sravanpant/files.txt")
# print(fp.read())

# fp = open("/home/sravanpant/files1.txt", "w")
# fp.write("Python")
# fp.close()

# to open in write mode and close file automatically

# with open("/home/sravanpant/files1.txt", "w") as outfile:
#     outfile.write("python")

# # to open in read mode and close file automatically
# with open("/home/sravanpant/files.txt", "r") as outfile:
#     print(outfile.read())

# with open("/home/sravanpant/files.txt", "r") as outfile:
#     print(outfile.read()) # reads the entire file and return it as string

# with open("/home/sravanpant/files.txt", "r") as outfile:
#     print(outfile.readline())  # this will read one line and return it as string

# with open("/home/sravanpant/files.txt", "r") as outfile:
#     print(outfile.readlines())  # this will read all the line and return it as list

# with open("/home/sravanpant/files2.txt", "w") as outfile:
#     outfile.write("Python")

# with open("/home/sravanpant/files2.txt", "r") as outfile:
#     print(outfile.read())

# with open("/home/sravanpant/files2.txt", "a") as outfile:
#     outfile.write("Elective")

# with open("/home/sravanpant/files2.txt", "r") as outfile:
#     print(outfile.read())

# with open("/home/sravanpant/files.txt", "r") as outfile:
#     for i in outfile:
#         print(i, end="")


# with open("/home/sravanpant/files.txt", "r") as outfile:
#     content = outfile.readline()
#     while content:
#         print(content, end="")
#         content = outfile.readline()

# with open("/home/sravanpant/files.txt", "r") as outfile:
#     print(outfile.read())

with open("/home/sravanpant/files.txt", "r") as outfile:
    print(outfile.readlines())
