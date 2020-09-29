# Составьте программу, получающую в командной строке 
# три целочислен­ных аргумента и выводящую слово 'equal ',
# если все три равны, и  'not equal'  в  противном случае. 

import sys

if len(sys.argv) == 4:
    firstArg = int(sys.argv[1])
    secondArg = int(sys.argv[2])
    thirdArg = int(sys.argv[3])

    if firstArg == secondArg == thirdArg:
        print('equal')
    else:
        print('not equal')