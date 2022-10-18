#         Задача
# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
#  С помощью использования "lambda", "list comprehension", "map"
#
#  Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 
#          Программа

def input_numbers ():
    while True :
        numb = input('введите число - ')
        try:
            numbers = int(numb)
            return numbers
        except:
            print('не число')

def create_tuple(a, b):
    return a,b

def int_r(num):                                  #  формула жесточащего округления для того чтобы было похоже на пример
    num = int(num + (1 if num > 0 else -0))
    return num

numbers=input_numbers()+1

formula_znach=lambda x: (1+int_r(1/x))**x
summa_num=lambda x: x+x

spisok_num=[int(n) for n in range(1, numbers)]
spisok_vichesl=[formula_znach(y) for y in range(1, numbers)]

dikt_numbers=map(create_tuple , spisok_num, spisok_vichesl)

print(f'словарь вычеслений со значениями согласно формулы - {dict(dikt_numbers)}')
print(f'сумма вычесленных значений - {sum(spisok_vichesl)}')
