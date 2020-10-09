#  Составьте  программу,  создающую точку,  случайно расположенную на единичном круге, но без использования оператора break. 
#  Сравните свое решение с таковым в конце этого раздела. 

import sys, math, random

def get_random_point():
    while True:
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        if math.sqrt(x ** 2 + y ** 2) < 1:
            return (round(x,2), round(y,2))

print ("Случайная точка на единичной окружности имеет координаты:",get_random_point())