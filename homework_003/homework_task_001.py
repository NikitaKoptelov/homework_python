#         Задача
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
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
    res_sum_num = 0
    for elem in range (len(numb)):
        if (elem % 2 != 0):
            res_sum_num += numb[elem]
    return res_sum_num


array_numbers = get_array_numb(input_numbers())
print(f'созданный список - {array_numbers}')
print(f'сумма чисел на нечетных позициях - {get_sum_num(array_numbers)}')

