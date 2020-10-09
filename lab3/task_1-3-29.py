# Составьте программу relativelyp rime .  ру,  получающую один аргумент командной строки n  и   
# выводящую таблицу n х n, где • устанавливается в строке i  и столбце j, если 
# наибольший общий делитель i и j состав­ляет 1  (i и j являются относительно простыми множителями), 
# и пробел в противном случае. 

import sys

a = int(sys.argv[1])
matrix = [["" for j in range(a)] for i in range(a)]

def gcd(x,y):
    while x!=0 and y!=0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x+y

for i in range(a):
    for j in range(a):
        if gcd(i,j) == 1:
            matrix[i][j] = '*'
        else:
            matrix[i][j] = ' '


for i in range(a):
    for j in range(a):
        print(matrix[i][j],end="")
        print (" ",end = "")
    print ("\n")