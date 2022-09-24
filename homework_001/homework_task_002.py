#         Задача
# Напишите программу для. 
# проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
#      программа


def get_numb (numb):
    if (0<numb<=7):
        return 'нет, не является выходным'
    else:
        return 'error'



numbers = int(input('введите цифру дня недели: '))
print (get_numb(numbers))

