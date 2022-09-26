#         Задача
# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
#  Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 
#          Программа


import math


def input_numbers ():
    while True :
        numb = input('введите число - ')
        try:
            numbers = int(numb)
            return numbers
        except:
            print('не число')

def get_array_numb (numb):
    array_numbers = dict()
    sym_array_num = 0
    for i in range (1, numb+1):
        array_numbers[i] = math.ceil(math.pow((1 + math.ceil(1/i)), i))
    for j in range (1, numb+1):
        sym_array_num += array_numbers.get(j)
    return array_numbers, sym_array_num



print (f'множества чисел {get_array_numb(input_numbers())[0]} - сумма множества - {get_array_numb(input_numbers())[1]}')
