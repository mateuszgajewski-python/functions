def add(): # musi byc bez parametrow gdy uzywamy global slowo
    global c # aby zmienic zmienna globalna
    c = c + 4
    print(c)


c = 1
add()
print(c)
