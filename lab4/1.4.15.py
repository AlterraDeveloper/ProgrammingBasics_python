import sys
import stdio
import stdarray


a=stdarray.create1D(3)
weights=[0.25, 0.25, 0.5]
#создание ряда оценок
for i in range(len(a)):
    k=int(input())
    a[i]=k
    #ввод каждой оценки
Avg=(a[0]*weights[0]*a[1]*weights[1]*a[2]*weights[2])/sum(weights)
#вычисление средневзвешенногозначения
stdio.writeln(Avg)