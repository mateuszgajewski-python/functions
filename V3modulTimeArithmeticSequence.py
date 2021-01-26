import time

x = 1000000

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



def czas_wykonania(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start


print(czas_wykonania(sumuj_do1,x))
print(czas_wykonania(sumuj_do2,x))
print(czas_wykonania(sumuj_do3,x))
print(czas_wykonania(sumuj_do4,x))
print(czas_wykonania(sumuj_do5,x))






