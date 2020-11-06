#  Составьте программу, вычисляющую произведение 
#  двух квадратных ма­триц логических переменных, 
#  используя оператор оr вместо + и  оператор and вместо *·

import random

arraySize = 4

def fillMatrixWithRandomBoolValues(array):
    array.clear()
    for i in range(0, arraySize):
        tmp = []
        for i in range(0, arraySize):
            tmp.append(random.randint(0,100) % 2 == 0)
        array.append(tmp)

def print_array(array):
    for row in array:
        for item in row:
            if(item): print( '*', end = ' ')
            else: print( '_', end = ' ')
        print()

def checkMatrixSize(matrix):
    size = len(matrix)
    if size == 0 : return False

    for row in matrix:
        if not len(row) == size: return False

    return True 

def addMatrix(matrix1, matrix2):
    if not (checkMatrixSize(matrix1) and checkMatrixSize(matrix2)):
        raise ArithmeticError('Для корректной работы метода нужны 2 квадратные матрицы одинакового размера')
    resultMatrix = []
    for i in range(0, len(matrix1)):
        tmp = []
        for j in range(0, len(matrix1)):
            tmp.append(matrix1[i][j] or matrix2[i][j])
        resultMatrix.append(tmp)
    return resultMatrix

def multiplyMatrix(matrix1, matrix2):
    if not (checkMatrixSize(matrix1) and checkMatrixSize(matrix2)):
        raise ArithmeticError('Для корректной работы метода нужны 2 квадратные матрицы одинакового размера')
    resultMatrix = []
    for i in range(0, len(matrix1)):
        tmp = []
        for j in range(0, len(matrix1)):
            tmp.append(matrix1[i][j] and matrix2[i][j])
        resultMatrix.append(tmp)
    return resultMatrix


firstArray = []
secondArray = []

fillMatrixWithRandomBoolValues(firstArray)
fillMatrixWithRandomBoolValues(secondArray)

print('first array = ')
print_array(firstArray)
print('second array = ')
print_array(secondArray)
print('Addition of matrix = ')
print_array(addMatrix(firstArray,secondArray))
print('Multiplication of matrix = ')
print_array(multiplyMatrix(firstArray,secondArray))



