def oldenough(old, name):
    if old >= 12:
        return name + " je dostatecne stary pro nakup! "
    else:
        return name + "je prilis mlady pro nakup! "
    
print(oldenough(11, "premysl"))
print(oldenough(16, "ota"))