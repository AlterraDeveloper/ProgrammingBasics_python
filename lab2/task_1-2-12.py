# Составьте программу,  получающую два положительных целых чис­ла в аргументах командной строки 
# и  выводящую False, если любой из них больше или равен сумме двух других, и  True в  противном случае. 
# (Примечание: этот код проверяет, могут ли эти три числа быть длинами сторон некоего треугольника.)

import sys

if len(sys.argv) == 4:
    result1 = (int(sys.argv[2]) + int(sys.argv[3])) > int(sys.argv[1]) 
    result2= (int(sys.argv[1]) + int(sys.argv[3])) > int(sys.argv[2]) 
    result3 = (int(sys.argv[1]) + int(sys.argv[2])) > int(sys.argv[3])

    print(result1 and result2 and result3) 