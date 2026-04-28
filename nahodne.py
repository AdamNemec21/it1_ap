import random 
cil = int(input("zadejte cislo: "))
pokusy = 0

while True:
    kostka1 = random.randint(1,100)
    kostka2 = random.randint(1,100)
    pokusy += 1 

    print("pokus", pokusy, ":", kostka1, kostka2)
    
    if kostka1 == cil and kostka2 == cil:
        print("obe kostky se =", cil, "po", pokusy, "pokusech")
        break