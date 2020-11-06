#  Расскажите, как программа 1.3.6 (sqrt. ру) реализует метод Ньютона при поиске квадратного корня. 
# Подсказка: используйте факт, что наклон каса­тельной к (дифференцируемой) функции fix) при х = t составляет f '(t). 
# Это позволяет найти уравнение касательной линии, а затем использовать его для поиска точки, 
# где касательная линия пересекает ось Х. Это позволяет использовать метод Ньютона для поиска корня 
# любой функции следую­щим образом: при каждой итерации заменяйте оценку t на t-fit) / f '(t). 

EPSILON = 1e-15

c = float(input()) #вводится c консоли
t = c
while abs(t - c/t) > (EPSILON * t):
    t = (c/t + t) / 2.0
print(t) 