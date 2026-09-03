import random

N = int(input("Enter the number of random points to generate: "))

n = 0
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        n = n + 1

    i = i + 1

pi = 4 * n / N

print("Approximate value of pi:", pi)