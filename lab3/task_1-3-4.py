# Улучшите решение упражнения 1.2.22, добавив код проверки аргументов командной строки 
# на принадлежность к диапазону допустимых для фор­мулы температуры воздуха 
# с учетом влияния ветра и код вывода сообще­ния об ошибке, если они не в диапазоне.

import sys
import math

if len(sys.argv) == 3:
    t = float(sys.argv[1])
    v = float(sys.argv[2])

    if math.fabs(t) < 50 and v > 3 and v < 120:
        w = 35.74 + 0.6215*t + (0.4275*t-35.75)*math.pow(v,0.16)
        print(w)
    else:
        print('t must be in (-50, 50) and v must be in (3, 120)')
    