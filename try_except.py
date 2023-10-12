# x = -1
# if x < 0:
#     raise Exception("no numbers less than zero")

# try:
#     k = 5 // 0
#     print(k)

# except ZeroDivisionError:
#     print("Cannot handle zero division")

# try:
#     l1 = [1, 2, 3]
#     print(l1[3])

# except IndexError:
#     print("Index going out of bound")

# try:
#     d = {"1": "aa", "2": "bb", "3": "cc"}
#     print(d[4])

# except KeyError:
#     print("Key does not exist")

# try:
#     x = int("xyz")
#     print(x)
# except ValueError:
#     print("Invalid value")

# try:
#     Sravan
# except NameError:
#     print("Name not defined")

# try:
#     x = "2" + 2
#     print(x)
# except TypeError:
#     print("Invalid type of data")


# try:
#     open("py.txt")

# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Completed")


# try:
#     a = int(input("Enter the value of a: "))
#     b = int(input("Enter the value of b: "))
#     c = a / b
#     print("ans a div b", c)
# except (ValueError, ZeroDivisionError):
#     print("Enter valid input")

# try:
#     raise IndexError
# except IndexError:
#     print("exception")
# try:
#     raise IndexError
# except:
#     print("exception")


def fn():
    try:
        raise ValueError
    except IndexError:
        print("Inner fn")


try:
    fn()
except ValueError:
    print("Outer fn")
