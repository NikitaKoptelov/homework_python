#         Задача
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#  Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# 
#          Программа


from itertools import count


def input_numbers ():
    while True :
        numb = input('введите число - ')
        try:
            numbers = int(numb)
            return numbers
        except:
            print('не число')

def get_array_numb (numb):
    array_numb = [int(x) for x in range(1, numb+1)]
    array_res_numb = [None] * numb
    resul_t = 1
    for i in range (len(array_numb)):
        for j in range (0, array_numb[i]):
            resul_t *= array_numb[j]
            array_res_numb[i] = resul_t
        resul_t = 1
    return array_res_numb



print (f'произведение множества чисел {get_array_numb(input_numbers())}')
