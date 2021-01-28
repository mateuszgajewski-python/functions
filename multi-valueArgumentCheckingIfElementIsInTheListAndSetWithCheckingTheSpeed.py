import time

def function_performance(func, *arg, **arg2): ### *arg - ktore sa nie nazwane, **arg - ktore sa nazwane
    sum = 0
    #print(arg[0]) #- mozna wejsc do pierwszego argumentu argumentu wielowarotsciowego za pomoca indexu
    #print(arg[1]) #- i do drugiego
    #w przypadku **arg
    #print(arg2) #- slownik
    #print(arg2.get("how_many_times"))  # - za pomoca nazwy odczytujemy wartosc 
    
    for i in range(0, arg2.get("how_many_times")):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]


def znajdzCzyNalezy(listLubzbior, arg):
    if arg in listLubzbior:
        return True
    else:
        return False



print(function_performance(znajdzCzyNalezy, setContainer, 999, how_many_times = 500000))
print(function_performance(znajdzCzyNalezy, listContainer, 999, how_many_times = 500000))

