#         Задача
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
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

def get_two_numb (num):
    numb_1 = 1
    numb_2 = 1
    fibo_nums = []
    for i in range(num):
        fibo_nums.append(numb_1)
        numb_1, numb_2 = numb_2, numb_1 + numb_2
    numb_1 = 0
    numb_2 = 1
    for i in range(num+1):
        fibo_nums.insert(0, numb_1)
        numb_1, numb_2 = numb_2, numb_1 - numb_2
    return fibo_nums


number = input_numbers()
print(f'числа негафибаначчи - {get_two_numb(number)}')

