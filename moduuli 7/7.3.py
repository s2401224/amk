numbers = {"EFHK":"Helsinki-Vantaa",
           "EGLL":"London-Heathrow",
           "LFPG":"Paris-Charles de Gaulle"}



print("1. Enter a new airport")
print("2. Fetch airport information")
print("3. Quit")

num = int(input("Enter ur choice: ")) 

while num != 3:
    if num == 1:
        icao = (input("Enter ICAO: "))
        name = (input("Enter airport: "))

        numbers[icao] = name

    elif num == 2:
        icao = (input("Enter ICAO: "))
        if icao in numbers:
            print(f"{icao}'s airport is {numbers[icao]}.")
        else:
            print("try again")
        

    num = int(input("Enter your choice: "))

    


