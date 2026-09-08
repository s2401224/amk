import random

holder = []

dice = int(input("How many dice to roll: "))

for x in range(dice):
    roll = random.randint(1, 6)
    holder.append(roll)

print("The sum of the dice is:", sum(holder))