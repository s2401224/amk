import random

num = int(input("How many sides does the dice have: "))
def dice_roll(num):
    return random.randint(1, num)

result = dice_roll(num)
print(result)

while result != num:
    result = dice_roll(num)
    print(result)