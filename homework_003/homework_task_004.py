#         Задача
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
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
    numb = ''
    res_two_numb = ''
    while num > 0:
        temp = num // 2
        if (temp * 2 == num):
            numb += '0'
        else:
            numb += '1'
        num //= 2
    j = len(numb) - 1
    for i in range(len(numb)):
        res_two_numb += numb[j]
        j-=1
    return res_two_numb


number = input_numbers()
print(f'обрабатываемое число - {number}')
print(f'двоичное число - {get_two_numb(number)}')

