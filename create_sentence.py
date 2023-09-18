List1 = input("Enter first list of words: ").split()
List2 = input("Enter second list of words: ").split()
List3 = input("Enter third list of words: ").split()

for k in range(len(List3)):
    for j in range(len(List2)):
        for i in range(len(List1)):
            print(List1[i] + " " + List2[j] + " " + List3[k])
