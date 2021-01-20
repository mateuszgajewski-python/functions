# return - zwrocic
x=1

def p_prost(a, b):
    return (a*b)

def o_prost(a, b):
    return 2*(a+b)


prostokaty =    [
    (1,9),
    (2,8),
    (3,7),
    (4,6),
    (5,5)
                ]


for sze, dlu in prostokaty:
    print("prostokat",
          x,
          " o obw :",
          o_prost(sze, dlu),
          " ma pole o pow :",
          p_prost(sze, dlu),
          "m2",
          "(",
          sze,
          'x',
          dlu,
          ")")
    x += 1




    
