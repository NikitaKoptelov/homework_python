#         Задача
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
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
    if (len(numb) % 2 != 0):
        len_array = (len(numb) // 2) + 1
    else:
        len_array = (len(numb) // 2)
    res_sum_num = [0] * len_array
    elem_ret = len_array + 1
    for i in range (0, len_array):
        res_sum_num[i] = numb[i] * numb[elem_ret]
        elem_ret -= 1
    return res_sum_num


array_numbers = get_array_numb(input_numbers())
print(f'созданный список - {array_numbers}')
print(f'произведение пар чисел - {get_sum_num(array_numbers)}')

