# Составьте программу, получающую два положительных целых числа в аргу­ментах командной строки и выводящую True, 
# если они делятся без остатка. 

import sys

firstNum = int(sys.argv[1])
secondNum = int(sys.argv[2])

print(firstNum % secondNum == 0)