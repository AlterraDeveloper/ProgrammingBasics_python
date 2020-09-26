# Составьте программу, получающую в аргументах командной строки пе­ременную t типа float 
# и выводящую результат вычисления выражения sin(2t) + sin(Зt). 

import sys
import math

if len(sys.argv) == 2:
    t = float(sys.argv[1])
    print(math.sin(2*t) + math.sin(3*t))
