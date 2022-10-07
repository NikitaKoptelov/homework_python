#         Задача
# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
# 
#          Программа


from math import pi

def input_numbers ():
    while True :
        numb = input('введите количество чисел после запятой - ')
        try:
            numbers = int(numb)
            if(1 <= numbers <= 10):
                return numbers
            else:
                print('за пределами числа')
        except:
            print('не число')

print(f'число ПИ - {pi}')

d = input_numbers()

okrug_pi = int(pi * (10 ** d)) / (10 ** d)

print(f'чмсло ПИ - {okrug_pi} , с числом знаков после запятой - {d}')

