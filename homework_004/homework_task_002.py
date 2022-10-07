#         Задача
# Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.
# 
#          Программа


def input_numbers ():
    while True :
        numb = input('введите число для разложения на множители - ')
        try:
            numbers = int(numb)
            return numbers
        except:
            print('не число')



def array_numbers (num):
    array_numb = []
    numb = 2
    while numb * numb <= num:
            if num % numb == 0:
                array_numb.append(numb)
                num//=numb
            else:
                numb += 1
    array_numb.append(num)
    return array_numb

numb = input_numbers()

print(f'число - {numb} - на множители - {array_numbers(numb)}')
