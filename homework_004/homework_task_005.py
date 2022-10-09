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

print(mnogochlen_1)
print(mnogochlen_2)

mnogochlen_1_spisok = [x for x in (mnogochlen_1.partition('=')[0]).split('+')]
mnogochlen_2_spisok = [x for x in (mnogochlen_2.partition('=')[0]).split('+')]

def razbor_mnogchlen (mnogochlen):
    mnogochlen_dect = {}
    x = len(mnogochlen)-1
    for i in range(0, len(mnogochlen)):
        mnogochlen_dect[x] = int((mnogochlen[i]).partition('x')[0])
        x-=1
    return mnogochlen_dect

mnogochlen_1_dect = razbor_mnogchlen(mnogochlen_1_spisok)
mnogochlen_2_dect = razbor_mnogchlen(mnogochlen_2_spisok)

if(len(mnogochlen_1_dect)>len(mnogochlen_2_dect)):
    for i in range(len(mnogochlen_2_dect), len(mnogochlen_1_dect)):
        mnogochlen_2_dect[i] = 0
elif(len(mnogochlen_2_dect)>len(mnogochlen_1_dect)):
    for i in range(len(mnogochlen_1_dect), len(mnogochlen_2_dect)):
        mnogochlen_1_dect[i] = 0

def summa_mnogochlen (mnogochlen_1, mnogochlen_2):
    resultat_mnogochlen = ''
    x = len(mnogochlen_1)-1
    for i in range(0, len(mnogochlen_1)):
        if(x>1):
            resultat_mnogochlen += f'{(mnogochlen_1[x] + mnogochlen_2[x])}x^{x}'
        elif(x==1):
            resultat_mnogochlen += f'{(mnogochlen_1[x] + mnogochlen_2[x])}x'
        elif(x==0):
            resultat_mnogochlen += f'{(mnogochlen_1[x] + mnogochlen_2[x])}'
        if(x>0):
            resultat_mnogochlen+= '+'
        x-=1
    else:
        resultat_mnogochlen+= '=0'
    return resultat_mnogochlen

res_mnogochlen = summa_mnogochlen(mnogochlen_1_dect, mnogochlen_2_dect)
print(res_mnogochlen)

fail = open('/media/nik/Disk_2/lesson_Python/homework_python/homework_004/summa_mnogochlenov.txt', 'w')
fail.write(res_mnogochlen)
fail.close()
