import time

def function_performance(func, listOrSet, arg, how_many_times = 1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(listOrSet, arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

#funkcja, czy 30 znajduje sie w set i list


def znajdzCzyNalezy(listLubzbior, arg):
    if arg in listLubzbior:
        return True
    else:
        return False



print(function_performance(znajdzCzyNalezy, setContainer, 999, 500000))
print(function_performance(znajdzCzyNalezy, listContainer, 999, 500000))

