number = int(input("enter numbers: "))

num = []

for n in range(1,number + 1,1):
    if number % n == 0:
        num.append(n)
if len(num) == 2:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")




