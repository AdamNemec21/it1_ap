import random

unik = False
pokusy = 3

# vygeneruje náhodný kód 0–10
tajny_kod = str(random.randint(0, 10))

while pokusy > 0 and not unik:

    print("mas", pokusy, "pokusy")
    print("1 - prohledat stul")
    print("2 - zkusit otevrit dvere")
    print("3 - podivat se pod koberec")

    volba = input("co udelas ? ")

    if volba == "1":
        print("nasel si kod. Skvele !")
        print(tajny_kod)

    elif volba == "2":
        kod = input("zadejte kod: ")
        if kod == tajny_kod:
            unik = True
        else:
            print("spatny kod")
            pokusy -= 1   # oprava (odečte 1 pokus)

    elif volba == "3":
        print("nic tu neni")

    else:
        print("neplatna moznost")

if unik:
    print("Unikl jsi")
else:
    print("prohral si, spravny kod byl"), print(tajny_kod)