#                   Задача: 
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
#        Программа

# nabor_simvol = input('ввидите набор повторяющихся символов - ')

#                     1      234     5 6   7    8      9    10 11
#                     7      711     6 2   4    5      7     61
#                         1111111111222222222233333333334444444
#               01234567890123456789012345678901234567890123456

nabor_simvol = 'ggggggghhhhhhhshffffffggtttt44444ooooooollllllo'
print(nabor_simvol)

num_por_simvol = 1
num_simvol = 1
i = 0 
slovar_simvol = {}
zip_stroka = ''
for n in range(i+1,len(nabor_simvol)):
    if(nabor_simvol[i] == nabor_simvol[n]):
        num_simvol+=1
    else:
        slovar_simvol[num_por_simvol] = {num_simvol : nabor_simvol[i]}
        zip_stroka+= f'{num_simvol}{nabor_simvol[i]}'
        i=n
        num_simvol = 1
        num_por_simvol+=1
        if(i==len(nabor_simvol)-1):
            num_simvol = 1
            slovar_simvol[num_por_simvol] = {num_simvol : nabor_simvol[i]}
            zip_stroka+= f'{num_simvol}{nabor_simvol[i]}'

print(slovar_simvol)
print(zip_stroka)

un_zip_stroka = ''
num = 0
for index in range(1, len(slovar_simvol)+1):
    for n in str((slovar_simvol[index]).keys()):
        if(n.isdigit()):
            num=int(n)
    un_zip_stroka+= f'{slovar_simvol[index][num] * num}'

print(un_zip_stroka)

