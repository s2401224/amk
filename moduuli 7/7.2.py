names = set()

name = input("Enter the name or enter to quit: ")


while name != "":

    if name in names:
        print("Existing name.")
    else:
        names.add(name)
        print("New name.")

    name = input("Enter the name or enter to quit: ")
for g in names:
    print(g)
