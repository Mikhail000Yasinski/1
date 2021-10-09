import math #импортируем модуль math для последующей работы с тригонометрическими функциями 
import numpy #импортируем модуль numpy для работы с массивами, которые изначально не реализованы в Python
import matplotlib.pyplot as mpp #импортируем matplotlib для реализации графического представления данных (графики, диаграммы и прочее) 

# Эта программа рисует график функции, заданной выражением ниже

#определим переменные ещё до запуска основных операций 
start_number = 0 #число, которое является началом интервала. 
stop_number = 200 #число, определяющее конец интервала
step = 0.1 #число, определяющее шаг (интервал между значениями)

def plot_func(a_value:float): #отдельно реализовали функцию вычисления значения относительно каждого элемента массива arguments, рассчитывая на масштабируемость программы
    '''
    также ожидаем, что a_value является float, хотя на самом деле может передаваться любой тип данных. Но в нашем случае
    возможны два варианта: целочисленное число или число с плавающей запятой/точкой.
    Зависит все от параметра step
    '''
    return math.sin(a_value)*math.sin(a_value/20.0) #возвращаем значение из функции, вычисляемое по формуле sin(a)*sin(a/20.0)


if __name__== '__main__': #проверка, запускается ли программа напрямую (нельзя запустить из другого файла)
    arguments = numpy.arange(start_number, stop_number, step) #создание одномерного массива с равномерно разнесенными (на конкретный шаг) значениями внутри заданного интервала.
    mpp.plot( 
        arguments,
        [plot_func(a) for a in arguments]
    )
    '''
    mpp.plot(...) позволяет построить график.
    Данная операция может принимать 0 аргументов и вывести пустой график.
    В нашем случае мы передаем два аргумента:
    - одномерный массив arguments, которые характеризуют ось абсцисс
    - соответствующие значения, откладываемые на оси ординат, генерируемые
    таким образом, что каждый элемент данного списка вычислен согласно функции plot_func(a_value)
    '''
    mpp.show() #операция графического показа графика средствами matplotlib
