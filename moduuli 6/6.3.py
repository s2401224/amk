
num = float(input("How many gallons: "))
def trans(gallons):
    return gallons * 3.78541


while num >= 0:
    
    result = trans(num)
    print(result)
    num = float(input("How many gallons: "))

else:
    print("fahhh")