def ocinka(a):
    if a > 89:
        return "відмінно"
    elif a > 69:
        return "добре"
    elif a > 49:
        return "задовільно"
    elif a > -1:
        return "незадовільно"
    else:
        return "а що тут введено"
while True:
    try:
        d = int(input("Введіть оцінку"))
    except ValueError:
        print("що це?")
    else:
        print(ocinka(d))