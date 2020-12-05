import sys,random, math

def evaluate(A, x):
    p = A[-1]
    i = len(A) - 2
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p

x = 1
print(evaluate([1/120,1/24,1/6,1/2,1,1],x))
print (math.exp(x))