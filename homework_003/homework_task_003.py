#         Задача
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
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

def get_array_numb (num):
    numb = [0] * num
    for i in range(len(numb)):
        numb[i] = round(random.uniform(0, len(numb)-1), 2)
    return numb

def get_sum_num (numb):
    res_raznic = 0
    numb_minim = (numb[0] % 1)
    numb_maxim = (numb[0] % 1)
    for i in range (0, len(numb)):
        if (numb_maxim < (numb[i] % 1)):
            numb_maxim = numb[i] % 1
        if (numb_minim > (numb[i] % 1)):
            numb_minim = numb[i] % 1
    res_raznic = numb_maxim - numb_minim
    return int(res_raznic * 100) / 100


array_numbers = get_array_numb(input_numbers())
print(f'созданный список - {array_numbers}')
print(f'разница мин и макс дробной части - {get_sum_num(array_numbers)}')

