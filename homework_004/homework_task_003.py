#         Задача
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# 
#          Программа

import random

def input_numbers ():
    while True :
        numb = input('введите число для последовательности чисел - ')
        try:
            numbers = int(numb)
            return numbers
        except:
            print('не число')

def array_numbers (num):
    array_numb = [random.randint(0, num) for i in range(0, num)]
    array_numb_unifi = list(set(array_numb))
    return (array_numb, array_numb_unifi)

numb = input_numbers()

print(f'список последовательности чисел - {array_numbers(numb)[0]} \n уникальный список последовательности чисел - {array_numbers(numb)[1]}')
