# Составьте фрагмент кода для создания двумерного массива Ь[ ][ ], 
# явля­ющегося транспозицией существующего массива а[ ] [] размером т х п. 

def print_array(array):
    for row in array:
        for item in row:
            print(item, end=' ')
        print()

m = 5
n = 3

a = []
b = []

for i in range (0, m):
    tmp = []
    for j in range (0, n):
        tmp.append(i+j)
    a.append(tmp)

for i in range (0, n):
    tmp = []
    for j in range (0, m):
        tmp.append(0)
    b.append(tmp)

print('a = ')
print_array(a)

for i in range(0, n):
    for j in range(0, m):
        b[i][j] = a[j][i]

print('\nb = ')
print_array(b)