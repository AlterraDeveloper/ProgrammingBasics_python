#  Составьте программу, получающую в аргументах: командной строки два це­лых числа, а и Ь, 
#  и выводящую случайное целое число в диапазоне от а до Ь. 

import random
import sys
if len(sys.argv) == 3:
    numStart = int(sys.argv[1])
    numEnd = int(sys.argv[2])

    print(random.randint(numStart, numEnd))