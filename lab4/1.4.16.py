import sys
import stdio
import stdarray
import random
import pdb

arow=int(sys.argv[1])
acol=int(sys.argv[2])
brow=int(sys.argv[3])
bcol=int(sys.argv[4])
#задаются размерности матриц

a=stdarray.create2D(arow,acol,random.randint(1,10))
b=stdarray.create2D(brow,bcol,random.randint(1,10))
#создается две рандомные матрицы

if acol != brow:
    stdio.writeln("Cannot multiply the two matrices. Incorrect dimensions.")
#проверяется на условия выполнения произведения

C = [[0 for row in range(bcol)] for col in range(arow)]
#задается нулевая матрица в которую будет записываться результат произведения

for i in range(arow):
    for j in range(bcol):
        for k in range(acol):
            pdb.set_trace()
            C[i][j] += a[i][k] * b[k][j]
            #выполняется произведение двух матриц

stdio.writeln(C)
#показывается результат выполнения произведения матриц