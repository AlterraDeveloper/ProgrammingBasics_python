# В отличие от гармонических чисел, сумма последовательности 1/12 + 1/22 + + ... + 1/п2 действительно сходится к 
# константе при п, стремящемся к бес­конечности. (Поскольку эта константа -тr2/6, данная формула использу­ется для вычисления 
# значения числа л.) Какой из следующих циклов for вычисляет эту сумму? 
# Подразумевается, что n -это целое число 1000000, а переменная total типа float инициализирована значением О. О. 
# а. for  i in range( 1, n+1 ): total +=  1  / (i•i) 
# Ь. for i  in  range(1, n+1 ): total +=  1.0 /  i•i 
# с.  for i  in  range( 1,  n+1 ): total +=  1.0 /  (i•i) 
# d. for i  in range(1, n+1 ): total +=  1.0 /  (1.0•i•i) 

total = 0.0
n = 1000000

for i in range(1, n + 1):#это тот цикл
    total += 1 / (i * i)
print('loop1=', total) 

total = 1.0
for i in range(1, n + 1):
    total += 1.0 / i * i
print('loop2=', total)

total = 1.0
for i in range(1, n + 1):
    total += 1.0 / (i * i)
print('loop3=', total)

total = 1.0
for i in range(1, n + 1):
    total += 1.0 / (1.0*i * i)
print('loop4=', total)
