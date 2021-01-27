def greet1(name, message):
    print(message, name)

greet1("Arek", "Witojcie")

def greet2(name, message):
    print(message, name)

greet2(name = "Arek", message = "Witojcie")

def greet3(name, message):
    print(message, name)

greet3(message = "Witojcie", name = "Arek",)

def greet4(name, message):
    print(message, name, sep="&&&" )

greet4("Arek", "Witojcie")

def greet5(name, message):
    print(message, name, sep="\n" )

greet5("Arek", "Witojcie")

def greet6(name, message, separator= " "):
    print(message, name, sep=separator)

greet6("Arek", "Witojcie", "\n")
