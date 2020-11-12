import  math
x = [1, 9, 11,144]
y = [4, 7, 34,343]
formula = 0
for i in range (0, len(x)-1):
     formula+= (x[i]-y[i])**2
print(math.sqrt(formula))
