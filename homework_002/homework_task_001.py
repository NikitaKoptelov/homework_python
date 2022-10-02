#         Задача
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Пример:
# - 6782 -> 23
# - 0,56 -> 11
#          Программа


def input_numbers ():
    while True :
        numb = input('введите число - ')
        try:
            numbers = float(numb)
            return numbers
        except:
            print('не число')

def get_sum_numb (numb):
    array_numb = [int(x) for x in str(numb) if x.isdigit()]
    summa_numbers = 0
    for i in range (len(array_numb)):
        summa_numbers += array_numb[i]
    return summa_numbers



print (f'сумма цифр в числе {get_sum_numb(input_numbers())}')
