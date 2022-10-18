#         Задача
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# с использованием функции "filter" и "list comprehension"
# 
#          Программа

import random

numbes_spisok = [random.randint(0, 20) for n in range(0,10)]
print(numbes_spisok)

def filtr_numbs_spisok (num):
    len_num=0
    count_num=0
    while len_num!=len(numbes_spisok):
        if(num==numbes_spisok[len_num]):
            count_num+=1
        len_num+=1
    if(count_num>1):
        return False
    else:
        return True

filt_num_spisok = list(filter(filtr_numbs_spisok, numbes_spisok))

print(filt_num_spisok)