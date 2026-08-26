gen = (input("whats ur biological gender, male or female?: "))
if gen == "male":
    hemo1=int(input("Whats ur hemoglobin value (g/l)?:"))
    if hemo1 < 134:
        print("to low sir")
    elif 134 < hemo1 < 167:
        print("Hell ye boy, things go great. Have a nice day")
    else:
        print("too high son, you gonna die soon")
elif gen == "female":
    hemo2=int(input("Whats ur hemoglobin value (g/l)?:"))
    if hemo2 < 117:
        print("It is too low for you, madam")
    elif 117 < hemo2 < 155:
        print("everything is great, madam. Have a great day")
    else:
        print("too high girl, survive okei?")
else:
    print("Stop tripping me. Just choose ur gender")