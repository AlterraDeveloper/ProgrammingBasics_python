# Составьте фрагмент кода, преобразующий двоичное представление по­ложительного целого числа n в строку s. 

import sys

number =  int(sys.argv[1])

str_bin_number = ''

while number != 0:
    str_bin_number += str(number % 2)
    number //= 2

print(str_bin_number[::-1])