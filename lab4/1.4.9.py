a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('a', a)
b = [x[:] for x in a]
print('b', b)

a = [[1, 2, 3], [4, 5, 6]]
print('a', a)
b = [x[:] for x in a]
print('b', b)

a = [[1, 2, 3, 4, 5], [6, 7, 8]]
print('a', a)
b = [x[:] for x in a]
print('b', b)