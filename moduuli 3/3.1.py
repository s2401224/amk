cm = int(input("What is the length of a zander?: "))
if cm < 42:
    print(f"The fish is {42 - cm} centimeters below the size limit.")
    print("Release the fish back into the lake.")
else:
    print("The fish is big enough to keep.")