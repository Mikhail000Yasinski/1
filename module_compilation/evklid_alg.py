import math

a, b = (int(i) for i in input("Введите два числа через пробел: ").split())
def gspd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b

print (gspd(a, b))

