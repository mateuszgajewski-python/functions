def w_powitalna(imie, wiek):
    print("Witaj", imie, "masz :", wiek, "lat(a)")

list_uzytkownikow = {"Kamil" : 18, "Adam" : 19, "Karol" : 40}

for key in list_uzytkownikow:
    w_powitalna(key, list_uzytkownikow[key])
    
