#  Составьте программу, выводящую сумму двух случайных целых чисел от 1 до 6 (как при бросании кубика).

import random

fstNum = random.randint(1,6)
sndNum = random.randint(1,6)
summ = fstNum + sndNum

print('Первый кубик: ' + str(fstNum))  
print('Второй кубик:' + str(sndNum))
print('Сумма: ' + str(summ))