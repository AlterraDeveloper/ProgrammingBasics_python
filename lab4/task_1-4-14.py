#  Составьте программу, получающую из командной строки целое число n и 
#  создающую массив а размером п х п элементов логического типа таким образом, 
#  чтобы элемент a[i][j] содержал значение True, если значения i  и  j  
#  являются взаимно простыми (relatively prime), т.е. не имеющими общих делителей,
#   и  False в  противном случае. Затем выведите массив (см. упр. 1.4.5), 
#   используя  *   для представления значений True и пробел для False. 
#   Выводите также номера рядов и столбцов. Подсказка: исполь­зуйте решето Эратосфена. 

import math
import sys

def fillMatrixWithPrimes(array, arraySize):
    array.clear()
    for i in range(0, arraySize):
        tmp = []
        for j in range(0, arraySize):
            tmp.append(checkPrime(i,j))
        array.append(tmp)

def print_array(array):
    for i in range(0, len(array)+1):
        if i == 0: print('  ', end='')
        else: print(i, end=' ')
    print()
    iter = 1
    for row in array:
        print(iter,end=' ')
        for item in row:
            if(item): print( '*', end = ' ')
            else: print( '_', end = ' ')
        print()
        iter = iter + 1

def checkPrime(number1, number2):
    return math.gcd(number1,number2) == 1

if len(sys.argv) != 2:
    print('Укажите число после названия файла')
    exit()

arraySize = int(sys.argv[1])
array = []
fillMatrixWithPrimes(array, arraySize)
print_array(array)





