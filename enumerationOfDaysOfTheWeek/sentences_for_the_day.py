import sentences
from enum import Enum

Dzien = Enum('Dni_Tygod nia','poniedzialek wtorek sroda czwartek piatek sobota niedziela')

while(1):

    print("""
Wybierz dzien tygonia
1 - poniedzialek
2 - wtorek
3 - sroda
4 - czwartek
5 - piatek
6 - sobota
7 - niedziela
0 - exit\n""")

    ch = int(input())

    if      ch == Dzien.poniedzialek.value:
            sentences.poniedzialek()
        
    elif    ch == Dzien.wtorek.value:
            sentences.wtorek()
        
    elif    ch == Dzien.sroda.value:
            sentences.sroda()
        
    elif    ch == Dzien.czwartek.value:
            sentences.czwartek()
        
    elif    ch == Dzien.piatek.value:
            sentences.piatek()
        
    elif    ch == Dzien.sobota.value:
            sentences.sobota()
        
    elif    ch == Dzien.niedziela.value:
            sentences.niedziela()

    elif    ch == 0:
            print("Koniec programu")
            break

    else:   print('err')
