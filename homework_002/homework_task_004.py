#         Задача
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# 
#          Программа

import random

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
    for i in range (1, numb+1):
        array_numbers[i] = random.randint((numb * -1), numb)
    return array_numbers



print (f'множества чисел {get_array_numb(input_numbers())}')
