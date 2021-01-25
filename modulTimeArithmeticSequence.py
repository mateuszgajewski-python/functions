import time

x = 100000000

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


print("Suma ciagu arytmetycznego od 1 do ",x, "1 + 2 + 3 + ... +",x)

print("--------------------------------------------------------------------------------")


start = time.perf_counter()
s1=sumuj_do1(x)
end = time.perf_counter()
print("funkcja z petla\t\t",    "|\t",s1,'\t|\t', (end - start),"sekund")
print("--------------------------------------------------------------------------------")


start = time.perf_counter()
s2=sumuj_do2(x)
end = time.perf_counter()
print("lista wyrazeniowa\t",    "|\t",s2,'\t|\t', (end - start),"sekund")
print("--------------------------------------------------------------------------------")


start = time.perf_counter()
s3=sumuj_do3(x)
end = time.perf_counter()
print("zbior wyrazeniowy\t",    "|\t",s3,'\t|\t', (end - start),"sekund")
print("--------------------------------------------------------------------------------")


start = time.perf_counter()
s4=sumuj_do4(x)
end = time.perf_counter()
print("generator\t\t",          "|\t",s4,'\t|\t', (end - start),"sekund")
print("--------------------------------------------------------------------------------")


start = time.perf_counter()
s5=sumuj_do5(x)
end = time.perf_counter()
print("wzor na ciag ary\t",     "|\t",s5,'\t|\t', (end - start),"sekund")
print("--------------------------------------------------------------------------------")
