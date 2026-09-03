
login = input("Enter your username: ")
password = input("Enter your password: ")
trial = 1

while login != "python" or password != "rules":
    if trial == 5:
        print("Access denied.")
        break
    print("Incorrect username or password. Please try again.")
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    trial = trial + 1

if login == "python" and password == "rules":
    print("Welcome")

