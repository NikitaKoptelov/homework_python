#         Задача
# Задана натуральная степень k. 
# Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#  Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 
#          Программа

import random

def input_numbers ():
    while True :
        numb = input('введите степень многочлена К - ')
        try:
            numbers = int(numb)
            return numbers
        except:
            print('не число')

step_k = input_numbers()

stroka_uravnen = ''

for step in range(step_k, -1, -1):
    kof_mnogch = random.randint(0,100)
    if(step>1):
        stroka_uravnen+= f'{kof_mnogch}x^{step}'
    elif(step==1):
        stroka_uravnen+= f'{kof_mnogch}x'
    else:
        stroka_uravnen+= f'{kof_mnogch}'
    if(step_k>=step>0):
        stroka_uravnen+= '+'
else:
    stroka_uravnen+= '=0'


print(stroka_uravnen)

fail = open('/media/nik/Disk_2/lesson_Python/homework_python/homework_004/многочлен степени k.txt', 'w')
fail.write(stroka_uravnen)
fail.close()




