#         Задача
# Реализуйте алгоритм перемешивания списка.
# 
#          Программа

import random
from re import L

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

def get_smesh_array_index (numb):
    array_numb=[int(x) for x in range(0, len(numb))]
    array_poz=[0]*len(array_numb)
    a=len(array_numb)-1
    array_poz[0]=random.randint(array_numb[0], array_numb[a])

    for i in range(a):
        i+=1
        j=i
        array_poz[i]=random.randint(array_numb[0], array_numb[a])
    
        while j>0:
            j-=1
            if array_poz[i]==array_poz[j]:
                array_poz[i]=random.randint(array_numb[0], array_numb[a])
                j=i

    return array_poz



array_numb = get_array_numb(input_numbers())
print(f'множества чисел       {array_numb}')
array_index = get_smesh_array_index(array_numb)
print(f'индекс перемешивания - {array_index}')

res_t_array = [0] * len(array_numb)
for i in range(0, len(array_numb)):
    res_t_array[i] = array_numb[array_index[i]]
print(f'перемешанный массив - {res_t_array}')

