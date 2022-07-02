import random
from random import randint
import time

"""
СТАРТ:
1)Создание первоначальной популяции (хромосомы с генами из 0 и 1)
2)Отбор хромосом с наибольшим количеством единиц
3)Скрещивание подходящих хромосом
4)Мутирование новых хромосом с целью в некотором поколении собрать хромосомы из одних 1
СТОП.

Алгоритм позаодяерт найти решение для уравнений вида
x1 + ... xn = n при должной модернизации))
В данном случае, фактически, решаем уравнение
x1 + x2 + x3 + x4 + x5 = 5

"""
class GenAlg:
    def __init__(self, gen_num, chromosome_num, mutation_chance, limit):
        GenAlg_result = 0
        l = self.population_inizialization(gen_num, chromosome_num)
        print('Start: ')
        for i, chromosome in enumerate(l):
            print(f'#{i} {chromosome} summ: {sum(chromosome)}')
        
        l, probabilities = self.fit_function(l)
        for j in range(limit):
            _l = self.cross(l)
            _l = self.mutation(_l, mutation_chance)
            _l, probabilities = self.fit_function(_l)
            l = _l
        print('Result: ')
        for i, chromosome in enumerate(l):
            print(f'#{i} {chromosome} summ: {sum(chromosome)}')
            self.GenAlg_result = sum(chromosome)
            
    def population_inizialization(self, gen_num, chromosome_num):
        '''
        Зарождение жизни!
        Создаём популяцию и возвращаем список популяции из
        хромосом и генов
        '''
        l = []
        for chromosome in range(chromosome_num):
            l.append([])
            for gen in range(gen_num):
                l[-1].append(randint(0, 1))
        return l
    
    def fit_function(self, l):
        '''
        Отбор!
        Функция работает как естественный отбор, только отбор искуственный)).
        Ищем хромосомы тех родителей, которых в дальнейшем будем скрещивать,
        рассчитывая шанс каждой особи на продолжение рода.
        '''
        values = {}
        for i, chromosome in enumerate(l):
            _summ = sum(chromosome)
            values[i] = _summ
            num_of_chromosome = len(chromosome)
        # Определяем насколько близко решение к требуемому результату и получаем вероятности
        _values = []
        for i in values:
            _values.append((values[i], i)) 
        probabilities = []
        total_sum = 0
        for _s, i in _values:
            total_sum = total_sum + _s
        for s, i in _values:
            probabilities.append((round(s / total_sum, 4), i))
        probabilities.sort(key = lambda tup: tup[0])
        
        probabilities = probabilities[len(probabilities) - num_of_chromosome:] # Выбираем лучший среди вариантов из популяции
        
        _l = []
        for precentage, index in probabilities:
            _l.append(l[index])
        return _l, probabilities
        
    def cross(self, l):
        '''
        Кроссинговер!
        Выбираем наиболее подходящие объекты и скрещиваем их в качестве родителей.
        Возвращаем новые особи.
        Здесь заданы 2 переменные, чтобы не выбрать одну и ту же особь дважды.
        '''
        _l = []
        for i, chromosome_i in enumerate(l):
            for k in range (i + 1, len(l)): 
                parent_1 = l[i]
                parent_2 = l[k]
                parent_1_new_right = l[k][len(l[i])//2:]
                parent_2_new_right = l[i][len(l[k])//2:]
                parent_1_new_left = l[i][:len(l[i])//2]
                parent_2_new_left = l[k][:len(l[k])//2]
                parent_1_new = []
                parent_1_new.extend(parent_1_new_right)
                parent_1_new.extend(parent_1_new_left)
                parent_2_new = []
                parent_2_new.extend(parent_2_new_right)
                parent_2_new.extend(parent_2_new_left)
                _l.append(parent_1_new)
                _l.append(parent_2_new)
        return _l
    
    
    def mutation(self, _l, mutation_chance):
        '''
        Мутирование!
        Изменяем хромосомы, полученных особей.
        '''
        mutation_chance = mutation_chance * 10 
        for i, chromosome in enumerate(_l):
            if randint(0, 100) <= mutation_chance:
                _l[i][randint(0, len(chromosome)) - 1] = randint(0, 1)
        return _l
    
start = time.perf_counter()
i = 1 
check = GenAlg(gen_num = 5, chromosome_num = 10, mutation_chance = 0.01, limit = i)
print(check.GenAlg_result)
while check.GenAlg_result != 5:
    i += 1
    check = GenAlg(gen_num = 5, chromosome_num = 10, mutation_chance = 0.01, limit = i)
print(f'finished in {round(time.perf_counter() - start)} sec')
