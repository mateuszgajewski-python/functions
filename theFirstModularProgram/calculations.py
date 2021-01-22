import calculatingTheAreaOfFigures

while(1):

    print("OBLICZANIE POWIERZCHNI\n")
    print("1 - kwadrat")
    print("2 - prostokat")
    print("3 - trojkat")
    print("4 - kolo")
    print("5 - trapez")
    print("exit aby wyjsc\n")

    ch = input("co wybierasz: ")

    if      ch == '1':      #Kwadrat
                            a = int(input("Podaj a: "))
                            print("\nKwadrat ma:", calculatingTheAreaOfFigures.pole_kwadratu(a), "\n")
                            
    elif    ch == '2':      #Prostokat
                            a = int(input("Podaj a: "))
                            b = int(input("Podaj b: "))
                            print("\nProstokat ma:", calculatingTheAreaOfFigures.pole_prostokata(a, b), "\n")
                            
    elif    ch == '3':      #Trojkat
                            a = float(input("Podaj a: "))
                            h = float(input("Podaj h: "))
                            print("\nTrojkat ma:", calculatingTheAreaOfFigures.pole_trojkata(a, h), "\n")
                            
    elif    ch == '4':      #Kolo
                            r = float(input("Podaj r: "))
                            print("\nKolo ma:", calculatingTheAreaOfFigures.pole_kola(r), "\n")
                            
    elif    ch == '5':      #Trapez
                            a = int(input("Podaj a: "))
                            b = int(input("Podaj b: "))
                            h = int(input("Podaj h: "))
                            print("\nTrapez ma:", calculatingTheAreaOfFigures.pole_trapezu(a, b, h), "\n")
                            
    elif    ch == "exit":   break

    else:                   print("ERROR")
    
