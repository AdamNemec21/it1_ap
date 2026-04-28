while True:
    x = int(input("Zadej první číslo: "))
    y = int(input("Zadej druhé číslo: "))
    op = input("Zadej operaci (+, -, *, /): ")

    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        if y != 0:
            print(x / y)
        else:
            print("Nelze dělit nulou")
    else:
        print("Neplatná operace")

    konec = input("přejete si ukončit program? Y/N ")
    if konec == "y" or konec == "Y":
        break
    