#                   Задача: 
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#
#        Программа

simvolu = 'уцожоцыапжыопджлоыфвпфтыдлфабвджэенэжгнелддне'
print(simvolu)

nabor_simvol = [x for x in simvolu.split('абв')]
print(''.join(nabor_simvol))
