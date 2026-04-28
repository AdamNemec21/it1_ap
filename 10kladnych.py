soucet = 0
max = -1

for i in range(10):
    cislo = int(input("zadejte cisla: "))
    soucet += cislo

print(soucet)

if cislo > max:
        max = cislo
        
print("Maxmum", max)