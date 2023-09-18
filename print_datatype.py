# Write program to print the datatype of the various objects created .
#!/usr/bin/env python3
import copy


string = "python"
string1 = copy.deepcopy(string)
string1 = string1 + "program"
print(string, string1)
numI = 123
numF = 123.232
numC = 1 + 2j
list1 = [1, 3, 45]
a = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 20]
tuple1 = (2, 2, 1)
boolean = True
none = None
print(a)
# print types
print(type(string))
print(type(numI))
print(type(numF))
print(type(numC))
print(type(list1))
print(type(tuple1))
print(type(boolean))
print(type(none))
