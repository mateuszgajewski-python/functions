import calculatingTheAreaOfFigures
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokat Trojkat Kolo Trapez Exit')
# print(list(Menu_Figury) - wypisuje liste
#Menu_Figury = IntEnum('Menu_Figury', ['Kwadrat', 'Prostokat', 'Trojkat', 'Kolo', 'Trapez', 'Exit'])
# - mozna przeslac bezposrednio liste
#Menu_Figury = IntEnum('Menu_Figury', {'Kwadrat' : 1, 'Prostokat' : 2, 'Trojkat' : 3, 'Kolo' : 4, 'Trapez' : 5, 'Exit' : 6})
# - mozna przeslac bezposrednio slownik i zmienic wartosci

while(1):

    print("OBLICZANIE POWIERZCHNI\n")
    print("1 - kwadrat")
    print("2 - prostokat")
    print("3 - trojkat")
    print("4 - kolo")
    print("5 - trapez")
    print("6 - aby wyjsc\n")

    ch = int(input("co wybierasz: "))

    if      ch == Menu_Figury.Kwadrat:      # z Enum musi być Menu_Figury.Kwadrat.value
                                        a = int(input("Podaj a: "))
                                        print("\nKwadrat ma:",
                                              calculatingTheAreaOfFigures.pole_kwadratu(a),
                                              "\n")
                            
    elif    ch == Menu_Figury.Prostokat:      
                                        a = int(input("Podaj a: "))
                                        b = int(input("Podaj b: "))
                                        print("\nProstokat ma:",
                                              calculatingTheAreaOfFigures.pole_prostokata(a, b),
                                              "\n")
                            
    elif    ch == Menu_Figury.Trojkat:      
                                        a = float(input("Podaj a: "))
                                        h = float(input("Podaj h: "))
                                        print("\nTrojkat ma:",
                                              calculatingTheAreaOfFigures.pole_trojkata(a, h),
                                              "\n")
                            
    elif    ch == Menu_Figury.Kolo:      
                                        r = float(input("Podaj r: "))
                                        print("\nKolo ma:",
                                              calculatingTheAreaOfFigures.pole_kola(r),
                                              "\n")
                            
    elif    ch == Menu_Figury.Trapez:      
                                        a = int(input("Podaj a: "))
                                        b = int(input("Podaj b: "))
                                        h = int(input("Podaj h: "))
                                        print("\nTrapez ma:",
                                              calculatingTheAreaOfFigures.pole_trapezu(a, b, h),
                                              "\n")
                            
    elif    ch == Menu_Figury.Exit:     break

    else:                               print("ERROR")
    
