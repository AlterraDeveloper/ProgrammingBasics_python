import math

def lg(n):
    if n<=0 : return 0
    return math.log(n,2)

print(lg(8))
print(lg(4))
print(lg(2))
print(lg(0))