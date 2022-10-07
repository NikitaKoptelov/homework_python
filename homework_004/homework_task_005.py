#         Задача
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# 
#          Программа

fail = open('/media/nik/Disk_2/lesson_Python/homework_python/homework_004/mnogochlen_1.txt', 'r')
mnogochlen_1 = fail.read()
fail.close()

fail = open('/media/nik/Disk_2/lesson_Python/homework_python/homework_004/mnogochlen_2.txt', 'r')
mnogochlen_2 = fail.read()
fail.close()

mnogochlen_1_slovar = dict()
mnogochlen_2_slovar = dict()

resultat_mnogochlen = ''

mnogochlen_1_spisok = [x for x in (mnogochlen_1.partition('=')[0]).split('+')]
mnogochlen_2_spisok = [x for x in (mnogochlen_2.partition('=')[0]).split('+')]
print(mnogochlen_1_spisok)
print(mnogochlen_2_spisok)

step_x_numb_1 = 0
num_1 = '^'
for index in range(0, len(mnogochlen_1_spisok)):
    for substring in num_1:
        if substring in mnogochlen_1_spisok[index]:
            # print(mnogochlen_1_spisok[index])
            step_x_numb_1 = index
            
        if substring in mnogochlen_2_spisok[index]:
            # print(mnogochlen_2_spisok[index])
            step_x_numb_2 = index
            break
resultat_mnogochlen+= str(int(mnogochlen_2_spisok[step_x_numb_2].partition('x')[0]) + int(mnogochlen_1_spisok[step_x_numb_1].partition('x')[0]) ) + 'x^2+'
mnogochlen_1_spisok.pop(step_x_numb_1)
mnogochlen_2_spisok.pop(step_x_numb_2)

num_2 = 'x'
for index in range(0, len(mnogochlen_1_spisok)):
    for substring in num_2:
        if substring in mnogochlen_1_spisok[index]:
            print(mnogochlen_1_spisok[index])
            step_x_numb_1 = index
            
        if substring in mnogochlen_2_spisok[index]:
            print(mnogochlen_2_spisok[index])
            step_x_numb_2 = index
            break
resultat_mnogochlen+= str(int(mnogochlen_2_spisok[step_x_numb_2].partition('x')[0]) + int(mnogochlen_1_spisok[step_x_numb_1].partition('x')[0]) ) + 'x+'
mnogochlen_1_spisok.pop(step_x_numb_1)
mnogochlen_2_spisok.pop(step_x_numb_2)
# print(mnogochlen_1_spisok)

numbers = 0
for i in range(0, len(mnogochlen_1_spisok)):
    numbers+= int(mnogochlen_1_spisok[i])
for i in range(0, len(mnogochlen_2_spisok)):
    numbers+= int(mnogochlen_2_spisok[i])

resultat_mnogochlen+= str(numbers) + '=0'


print(resultat_mnogochlen)

fail = open('/media/nik/Disk_2/lesson_Python/homework_python/homework_004/summa_mnogochlenov.txt', 'w')
fail.write(resultat_mnogochlen)
fail.close()
