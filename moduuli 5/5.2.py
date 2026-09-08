numbers = []

number = input("enter numbers or quit by pressing Enter: ")
while number!="":
    number = int(number)
    numbers.append(number)
    number = input("enter numbers or quit by pressing Enter: ")


numbers.sort(reverse=True)

print(numbers[:5])