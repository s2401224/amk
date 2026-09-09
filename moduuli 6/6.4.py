def fun(numbers):
    total = 0

    for x in numbers:
        total = total + x

    return total


numbers = [2, 5, 10 ]

result = fun(numbers)

print(result)