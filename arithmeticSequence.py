x = 1000

def sumuj_do1(liczba):
    suma = 0

    for liczba in range(1,liczba+1):
        suma = suma + liczba

    return suma


def sumuj_do2(liczba):
    
    return sum([liczba for liczba in range(1,liczba+1)])


def sumuj_do3(liczba):
    
    return sum({liczba for liczba in range(1,liczba+1)})


def sumuj_do4(liczba):
    
    return sum((liczba for liczba in range(1,liczba+1)))


def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba

print("----------------------------------------------")
print("funkcja z petla\t\t","|  ",        sumuj_do1(x))
print("----------------------------------------------")
print("lista wyrazeniowa\t","|  ",        sumuj_do2(x))
print("----------------------------------------------")      
print("zbior wyrazeniowy\t","|  ",        sumuj_do3(x))
print("----------------------------------------------")    
print("generator\t\t","|  ",              sumuj_do4(x))
print("----------------------------------------------")     
print("wzor na ciag ary\t","|  ",         sumuj_do5(x))
print("----------------------------------------------")      
