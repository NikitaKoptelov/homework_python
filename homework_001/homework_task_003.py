#         Задача
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
#   Пример:
#  - x=34; y=-30 -> 4
#  - x=2; y=4-> 1
#  - x=-34; y=-30 -> 3
#      программа


def get_numb (numb_x, numb_y):
    if (numb_x > 0 and numb_y > 0):
        return 'первая четверть координат'
    elif (numb_x < 0 and numb_y > 0):
        return 'вторая четверть координат'
    elif (numb_x < 0 and numb_y < 0):
        return 'третья четверть координат'
    elif (numb_x > 0 and numb_y < 0):
        return 'четвертая четверть координат'
    else:
        return 'error'



print ('введите координаты точки для определения четверти:')
numb_x = int(input('введите координату Х - '))
numb_y = int(input('введите координату Y - '))
print (get_numb(numb_x, numb_y))

