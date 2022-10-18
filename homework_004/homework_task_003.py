#         Задача
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# 
#          Программа

#                4  11  0  2  16  10     18        13  7  20      12  5     3  
numbes_spisok = [4, 11, 0, 2, 16, 10, 2, 18, 2, 2, 13, 7, 20, 10, 12, 5, 5, 3, 4, 11]

print(f'заданный список чисел - {numbes_spisok}')

for index in range(0,len(numbes_spisok)): 
    if(index<len(numbes_spisok)):
        n = index + 1
    for _ in range(index + 1, len(numbes_spisok)):
        if(numbes_spisok[index]==numbes_spisok[n]):
            numbes_spisok.pop(n)
            n-=1
        if(n==len(numbes_spisok)-1):
            break
        n+=1

print(f'список элементов исходной последовательности не повторяющийся - {numbes_spisok}')
