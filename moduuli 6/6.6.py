
import math

def pizza_calc(diameter, price):
    radius = diameter / 100 / 2
    area = math.pi * radius ** 2
    return price / area


pizza1_diameter = float(input("Diameter of pizza 1: "))
pizza1_price = float(input("Price of pizza 1: "))

pizza2_diameter = float(input("Diameter of pizza 2: "))
pizza2_price = float(input("Price of pizza 2: "))

price1 = pizza_calc(pizza1_diameter, pizza1_price)
price2 = pizza_calc(pizza2_diameter, pizza2_price)

if price1 < price2:
    print("Pizza 1 is better value for money")
else:
    print("Pizza 2 is better value for money")

