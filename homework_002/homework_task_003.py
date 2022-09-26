#         Задача
# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
#  Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
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
  



print (f'произведение множества чисел {get_array_numb(input_numbers())}')
