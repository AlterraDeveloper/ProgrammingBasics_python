import numpy
massiv = numpy.arange(8).reshape(2,2,2)

for i  in range(2):
    for j in range(2):
       for g in range(2):
          massiv[i][j][g]= False

print(massiv)