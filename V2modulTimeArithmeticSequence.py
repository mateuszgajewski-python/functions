import time

x = 10000000

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


def czas_wykonania(start):
    end = time.perf_counter()  # mało optymalne rozwiązanie, ulepszenie w V3
    return (end - start)
    



start = time.perf_counter()
print(sumuj_do1(x))
print(czas_wykonania(start))

start = time.perf_counter()
print(sumuj_do2(x))
print(czas_wykonania(start))

start = time.perf_counter()
print(sumuj_do3(x))
print(czas_wykonania(start))

start = time.perf_counter()
print(sumuj_do4(x))
print(czas_wykonania(start))

start = time.perf_counter()
print(sumuj_do5(x))
print(czas_wykonania(start))




