a = 4   #obiekt a

a.bit_length()   #metoda bit_length, nie dotyczy za bardzo tego co przerabiam, ale zapisałem sobie :)

listSample = [1, 4, 512, 24]


listSample2 = listSample

print("listSample:\t",listSample)
print("listSample2:\t",listSample2)

listSample2.append(465) #doda do listSample2 i do listSample bo mają ten sam adres w pamieci
listSample[0] = 7       #w obu listach zmieni sie zerowy element i bedzie miał wartosc 7
                        # listy są mutable

print("\nlistSample:\t",listSample)
print("listSample2:\t",listSample2)

print("\nAdres listSample:\t", id(listSample))
print("Adres listSample2:\t", id(listSample2))

a = 4
print("\nAdres a:\twartosc: ", a, "\tadres: ", id(a))

b = a #adres bedzie ten sam co zmiennej a bo przechowywana jest ta sam wartosc (optymalizacja)
print("Adres b:\twartosc: ", b, "\tadres: ", id(b))

b = 7 #adres zmiennej b ulegnie zmianie dopiero gdy wartosc bedzie inna niz w zmiennej a
print("Adres b:\twartosc: ", b, "\tadres: ", id(b))



k = 4 #adres obu zmiennych jest ten sam bo wskazuja na ten sam obiekt (optymalizacja), ten sam adres ma zmienna a i b kiedy przychowywala wartosc 4
h = 4

print("\nAdres k:\twartosc: ", k, "\tadres: ", id(k))
print("Adres h:\twartosc: ", h, "\tadres: ", id(h))

h = 25 #adres sie zmieni bo nie bedzie juz pokazywac na to co pokazuje zmienna k, a i b gdy ma wartosc 4
print("Adres h:\twartosc: ", h, "\tadres: ", id(h))

c = 5
print("\nAdres c:\twartosc: ", c, "\tadres: ", id(c))

def add(c, amount = 1):
    print("Adres c:\twartosc: ", c, "\tadres: ", id(c)) #do poki nie zaczniemy dzialac na c bedzie miala ten sam adres co zmienna globalna o tej nazwie
    c = c + amount #zaczynamy dzialac
    print("Adres c:\twartosc: ", c, "\tadres: ", id(c), "\n") #i zmienna zmienia adres bo int jest inmutable, nie zachodza zmiany na orginalach

add(c)
print("\n\n\n")

print("dodajElementDoListy\n")

def dodajElementDoListy(lista, element):
    print("Adres listy :\t", id(lista))
    lista.append(element)
    print("Adres listy :\t", id(lista),'\n') # tutaj lista nie zmienia adresu bo listy są mutable - są zmiany robione na orginalach

dodajElementDoListy(listSample, 1000)
dodajElementDoListy(listSample2, 1001)

print("\nlistSample:\t",listSample)
print("listSample2:\t",listSample2)

print("\nAdres listSample:\t", id(listSample))
print("Adres listSample2:\t", id(listSample2))

#obiekty immutable - bool, int, float, tuple, str



print("dodajElementDoListy2")
def dodajElementDoListy2(lista, element):
    print("Adres listy :\t", id(lista))
    lista.append(element)

    a = [2,5,6] # tworzenie nowej listy z nowym adresem
    lista = a # przypisanie zmiennej 'lista' adresu listy 'a' (teraz juz nie bedzie miala zmienna lista adresu z przeslanej listy bo ta z listy 'a' ja zastapila
    print("Adres listy :\t", id(lista),'\n') # wypisanie adresu lista takiego jak ma lista 'a', a nie przeslanej listy do funkcji


print("\n\n\n")


print("dodajElementDoListy2\n")
dodajElementDoListy2(listSample, 1000)
dodajElementDoListy2(listSample2, 1001)

print("\nlistSample:\t",listSample)
print("listSample2:\t",listSample2)

print("\nAdres listSample:\t", id(listSample))
print("Adres listSample2:\t", id(listSample2))











