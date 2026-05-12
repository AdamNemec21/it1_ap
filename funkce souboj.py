def souboj(utok,obrana):
    if utok > obrana:
        return "zasah"
    else:
        return "odrazeno"
        

print(souboj(10,5))
    