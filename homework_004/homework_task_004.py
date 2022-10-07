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

num_perem = random.randint(1, 10)
shag = 0
stroka_uravnen = ''
for _ in range(0, num_perem):
    kof_num_pere = random.randint(0, 100)
    if(0 < kof_num_pere <= 100):
        stroka_uravnen+= str(kof_num_pere)
    num_x_perem = random.randint(0,1)
    steprn_perem = random.randint(1,2)
    if(num_x_perem==1):
        stroka_uravnen+= 'x'
        if(steprn_perem == 2):
            stroka_uravnen+= '^2'
    shag+=1
    if(shag < num_perem):
        stroka_uravnen+= '+'
    if(shag==num_perem):
        stroka_uravnen+= ' = 0'

print(stroka_uravnen)

fail = open('/media/nik/Disk_2/lesson_Python/homework_python/homework_004/многочлен степени k.txt', 'w')
fail.write(stroka_uravnen)
fail.close()




