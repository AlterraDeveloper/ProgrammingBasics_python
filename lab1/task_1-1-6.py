import sys

if len(sys.argv) == 4:
    names = sys.argv[::-1]
    print('Hi ' + names[0] + ', ' + names[1] + ' and ' + names[2])
else:
    print('Give me 3 arguments...')

