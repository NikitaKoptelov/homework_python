#         Задача
# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними 
# в 2D пространстве.
#    Пример:
#  - A (3,6); B (2,1) -> 5,09
#  - A (7,-5); B (1,-1) -> 7,21
#      программа

import math

def get_numb (numb_a, numb_b):
    array_numb_a = [int(x) for x in numb_a.split()]
    array_numb_b = [int(x) for x in numb_b.split()]
    if (0 < len(array_numb_a) < 3 and 0 < len(array_numb_b) < 3):
        return round(math.sqrt(math.pow((array_numb_b[0] - array_numb_a[0]), 2) + math.pow((array_numb_b[1] - array_numb_a[1]), 2)), 3)
    else:
        return 'error'



print ('введите координаты двух точки для нахождения расстояния между ними в 2D:')
numb_a = input('введите координаты точки А через пробел - ')
numb_b = input('введите координату точки Б через пробел - ')
print (get_numb(numb_a, numb_b))
