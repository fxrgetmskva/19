def dodawanie(a,b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnożenie(a,b):
    return a * b

def działanie(a,b):
    if b == 0:
        return
    else: return a/b
Kalkulator = {"+":dodawanie,"-":odejmowanie,"*":mnożenie,"/":działanie}
u2 = float(input("Podaj liczbe a"))
u1 = float(input("Podaj liczbe b"))

działanie(Kalkulator[działanie](u1,u2))