


def fun(numbers):
    even = []

    for x in numbers:
        if x % 2 == 0:
            even.append(x)
    print(numbers)
    print(even)
    return even



numbers = [1, 2, 3, 4, 5]

fun(numbers)

