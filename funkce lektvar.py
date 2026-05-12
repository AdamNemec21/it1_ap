batoh = ["mec", "lektvar", "stit", "zlato", "lektvar"]

def pocet_lektvaru(inventar):
    pocet = 0
    for staff in inventar:
        if staff == "lektvar":
            pocet += 1
    return pocet

print("máš", pocet_lektvaru(batoh), "lektvarů")