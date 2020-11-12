lis = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lis = [list(reversed(x)) for x in zip(*lis)]
print(lis)