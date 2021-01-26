
def narysuj(func, arg):
    func(arg)


def kolo(arg):
    print("Koło ma,", arg)

def kwadrat(arg):
    print("Kwadrat ma,", arg)



narysuj(kolo, 3)
narysuj(kwadrat, 5)
narysuj(kolo, 6)
narysuj(kwadrat, 7)
