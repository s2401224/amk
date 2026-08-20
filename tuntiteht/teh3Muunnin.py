syote = input("kuinka monta grammaa: ")

gramm = int(syote)
kg = gramm // 1000
jaannos = gramm % 1000
print(str(kg) + "kg ja " + str(jaannos) + "gr")