# Составьте фрагмент кода, получающий два аргумента командной стро­ки 
# типа float и выводящую True, если оба находятся в диапазоне 
# от О. О до 1. О, и False в противном случае.

import sys

fstArg = float(sys.argv[1])
sndArg = float(sys.argv[2])

print((fstArg >= 0 and fstArg <= 1) and (sndArg >= 0 and sndArg <= 1))
