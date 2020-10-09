# Используя метод Ньютона, разработайте программу, получающую в ар­гументах командной 
# строки целые числа n и k и выводящую корень kth числа n (Подсказка: см. упр. 1.3.17.

EPSILON = 1e-15

n = int(input())
k = int(input())
kth = t = n
i = 1
while abs(t - n / t) > (EPSILON * t):
    if i == k:
        kth = t
        break
    t = (n / t + t) / 2.0
    i += 1
print('kth =', kth)
