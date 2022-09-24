#         Задача
# Напишите программу для. 
# проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
#      программа


def get_numb ():
    array = [0, 1]
    for x in array:
        for y in array:
            for z in array:
                if (-(x or y or z) == (-x and -y and -z)):
                    print(f'верное при значениях X - {x} Y - {y} Z - {z}')



print (get_numb())

