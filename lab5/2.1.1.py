# Составьте функцию mахЗ( ), получающую три аргумента типа int или
# float и возвращающую наибольший из них.

import math

def maxN(*arg):
    return max(args)
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b):
        return c


a = float(input('ВВедите значение а: '))
b = float(input('ВВедите значение b: '))
c = float(input('ВВедите значение c: '))

print('Max = ', max3(a,b,c))