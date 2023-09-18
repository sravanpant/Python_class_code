# Program to create 2 lists containing numbers;
# create a third list that will contain
# the multiples of 2 from the first list and
# multiples of 3 from the second list.

list1 = input("Enter a list of numbers: ")
list2 = input("Enter another list of numbers: ")
list1 = list1.split()
list2 = list2.split()
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]
list3 = [2 * x for x in list1] + [3 * x for x in list2]
print(list3)
