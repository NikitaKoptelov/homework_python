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
        numb[i] = random.randint(0, len(numb)-1)
    return numb

def get_sum_num (numb):
    res_sum_num = [0] * (len(numb) // 2)
    elem_ret = len(numb) - 1
    for i in range (0, (len(numb) // 2)):
        res_sum_num[i] = numb[i] * numb[elem_ret]
        elem_ret -= 1
    return res_sum_num


array_numbers = get_array_numb(input_numbers())
print(f'созданный список - {array_numbers}')
print(f'произведение пар чисел - {get_sum_num(array_numbers)}')

