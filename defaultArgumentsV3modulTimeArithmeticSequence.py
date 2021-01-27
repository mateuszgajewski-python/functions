import time


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



def czas_wykonania(func, arg, how_many_times =1):
    acc = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        acc = acc + (end - start)
    return acc


print(czas_wykonania(sumuj_do1,1000,3000))
print(czas_wykonania(sumuj_do2,1000,3000))
print(czas_wykonania(sumuj_do3,1000,3000))
print(czas_wykonania(sumuj_do4,1000,3000))
print(czas_wykonania(sumuj_do5,1000,3000))






