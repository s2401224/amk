num = input("any number: ")

if num != "":
    num = int(num)
    smallest = num
    largest = num

    while num != "":
        print(num)

        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

        num = input("any number: ")

        if num != "":
            num = int(num)
    print("Smallest:", smallest)
    print("Largest:", largest)