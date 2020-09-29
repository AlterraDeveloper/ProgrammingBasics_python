# Составьте более общую и надежную версию программы 
# 1.2.4 (quadratic. ру ), выводящую корни уравнения ах2 + Ьх + с, 
# выводящую соответствую­щее сообщение, если дискриминант отрицателен, 
# и принимающую соот­ветствующие меры, избегая деления на нуль.

import math 
import sys 

b = float(sys.argv[1])
с = float(sys.argv[2]) 

discriminant = b*b - 4.0 * с
if discriminant > 0:
    d = math.sqrt(discriminant) 
    print((-b  + d) /  2.0) 
    print((-b  -d) /  2.0)
elif discriminant == 0:
    print(-b / 2.0)
else:
    print('discriminant is negative')
