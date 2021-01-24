import sentenceColor
from enum import Enum

Kolor = Enum('Kolor','czerwony zielony niebieski menu exit')

sentenceColor.menu()

while(1):

    ch = int(input("Wybierz kolor: "))

    if ch == Kolor.czerwony.value:
        sentenceColor.czerwony()

    elif ch == Kolor.zielony.value:
        sentenceColor.zielony()

    elif ch == Kolor.niebieski.value:
        sentenceColor.niebieski()

    elif ch == Kolor.menu.value:
        sentenceColor.menu()

    elif ch == Kolor.exit.value:
        break

    else:
        print("err")
