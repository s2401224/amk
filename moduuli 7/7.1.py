seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter the number of a month: "))
print(seasons[(month % 12) // 3])
