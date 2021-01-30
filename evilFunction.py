print("""PROGRAM POKAZUJE CO SIE DZIEJE Z LISTA.
JAKA JEST PRZED WEJSCIEM DO FUNKCJI,
A JAKA PO WYJSCIU

JESLI NIE CHCEMY POTRACIC DANYCH Z LISTY NALEZY UWAZAC JAK SIE PRZEKAZUJE JĄ DO FUNKCJI

Listy są mutable i nie sa przekazywane kopie automatycznie,
tylko cały oryginal i na nim są wykonywane operacje.

Trzeba stosować kopie jesli nie chemy aby nasza lista ktora wysylamy ulegla BEZPOWROTNEJ zmianie,
chyba ze chcemy zmodyfikować liste i o tym wiemy. ZLOSLIWE FUNKCJE NIE SPIA


""")






def evil_function2(toBeDestroyedList):
    toBeDestroyedList[0] = 4
    print("local list\t\t", toBeDestroyedList)
    
myList2 = [1,4,2,1,52,3]
print("global list\t\t", myList2)

print("BEZ KOPII")
evil_function2(myList2) #lista bedzie zepsuta przez wysłanie jej do mało zaufanej funkcji.
                        #nastapiła zmiana bez powiadomienia nawet ze doszło do zmiany oryginalu, dane przepadły!!! !!!Musze byc  bardziej ostrozny nastepnym razem!!!
print("global list\t\t",myList2)


print("UTRATA DANYCH!!! - lista zmieniła sie na poziomie globalnym")
print("--------------------------------")






def evil_function3(toBeDestroyedList):
    print("global id list[0]\t", id(toBeDestroyedList[0])) #---
    toBeDestroyedList[0] = 4                                 #----- int jest immutable i adres sie zmieni, mimo kopi plytkiej
    print("local id list[0]\t", id(toBeDestroyedList[0]))  #---
    print("local list\t\t", toBeDestroyedList)

myList3 = [1,4,2,1,52,3]
print("global list\t\t", myList3)

print("KOPIA PLYTKA")
evil_function3(myList3.copy())  # przeslana bedzie kopia listy. oryginal nie bedzie przeslany (plytka kopia) lista skopiowana ma inny adres,
                                # ale wartosci list maja te same adresy. Gdy lista przechowuje immutible to jest OK. i plytka kopia wystarczy
                                # balagan zaczyna sie gdy przychowujemy w mutable mutable, np. Lista w liscie. Wtedy jest potrzeba kopia gleboka
print("global list\t\t", myList3)

print("OK!!!")
print("--------------------------------")








def evil_function4(toBeDestroyedList):
    print("global id list[0][0]\t", id(toBeDestroyedList[0])) #---
    toBeDestroyedList[0][0] = 20                             #------ list jest inmmutable i adres nie zmieni się. !!!Musze byc  bardziej ostrozny nastepnym razem!!!
    print("local id list[0][0]\t", id(toBeDestroyedList[0]))  #---
    print("local list\t\t", toBeDestroyedList)

myList4 = [[1,4],[2,1],[52,3]]
print("global list\t\t", myList4)

print("KOPIA PLYTKA")
evil_function4(myList4.copy())    #plytkie copy nie nadaje sie do list w liscie

print("global list\t\t", myList4)

print("UTRATA DANYCH!!! - lista zmieniła sie na poziomie globalnym")
print("--------------------------------")








#trzeba najpier ziportować copy
import copy


def evil_function5(toBeDestroyedList):
    print("global id list[0][0]\t", id(toBeDestroyedList[0][0])) #---
    toBeDestroyedList[0][0] = 20                             #------ kopiowane glebokie
    print("local id list[0][0]\t", id(toBeDestroyedList[0][0]))  #---
    print("local list\t\t", toBeDestroyedList)

myList5 = [[1,4],[2,1],[52,3]]
print("global list\t\t", myList5)

print("KOPIA GLEBOKA")
evil_function5(copy.deepcopy(myList5))    #gleboka kopia usuwa wade funkcji nr 4

print("global list\t\t", myList5)
print("OK!!!")




