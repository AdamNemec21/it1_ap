x = int(input("zadejte prvni cislo"))
y = int(input("zadejte druhe cislo ")) 

if x > y:
    #print(x + "je vetsi nez" + y)
    #print(x, "je vetsi nez" ,y)
    #print(str(x) + " je vetsi nez " + str(y))
    print(f"{x} je vetsi nez {y}")
elif x == y:
    print("zadana cisla jsou stejna")
else:
    print(f"{y} je vetsi nez {x}")
