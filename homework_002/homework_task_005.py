#         Задача
# Реализуйте алгоритм перемешивания списка.
# 
#          Программа


import random

array_numb = [int(x) for x in range(1, 6)]

def get_array_numb (num):
    num = [0] * len(num)
    for i in range(len(num)):
        num[i] = random.randint(0, len(num)-1)
    return num

def get_numb (numb):
    i = 0
    if numb[i] in numb:
        temp = random.randint(0, len(numb)-1)
        if temp not in numb: 
            numb[i] = temp
        else:
            get_numb(numb)
    i += 1
    if (i == len(numb)):
        i = 0
    return numb
    
array_poz_num = get_array_numb(array_numb)
print(get_numb(array_poz_num))