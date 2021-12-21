

s_p = [2]  # добавим двойку как очевидное первое простое число, это пригодится далее
n = 1949340  # число, до которого будем искать простые
for i in range(3, n + 1, 2): # перебираем числа, начиная с трёх и только чётные - двойка пригодилась
    m = 0  # задаём переменную для числа делителей нацело
    r = int(n**0.5) + 2  # достаточно перебирать только числа до корня из проверяемого, т.к остальные числа слишком близки к нему, чтобы не быть взаимно простыми - оптимизация!
    for j in s_p:   
        if j > r:             
            break
        if i % j == 0:  # проверяем делимость на простое число, которое уже попало в список
            m = 1  # если делится хотя бы на одно из списка, значит число не является простым
            break
    if m == 0:  # если делимости на простое из списка не обнаружилось, добавляем число в список
        s_p.append(i)

p = s_p[-1]  # Последнее число в списке простых будет либо n либо не n, это и проверим
if p == n:  
    print ("Простое!")
else:
    print ("Не простое!")
