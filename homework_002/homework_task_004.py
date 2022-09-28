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

def get_numb_file (numb):
    file = open('/media/nik/Disk_2/lesson_Python/homework_python/homework_002/file.txt', 'r')
    data = file.read().splitlines()
    res_t = 1
    for i in range(len(data)):
        j = int(data[i])
        res_t *= numb[j]
    print(f'данные из файла - {data}')
    return res_t


array_numb = get_array_numb(input_numbers())
print (f'множества чисел {array_numb}')
print(f'произведение позиций по заданию файла - {get_numb_file(array_numb)}')