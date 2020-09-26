# Студент-физик получил неожиданный результат при использовании кода force = G • mass1 • mass2 / radius * radius 
# для вычисления значения по формуле F = Gm1m2/r2• Объясните проблему и исправьте код. 

G = 10
mass1 = mass2 = 5
radius = 10
forceFstCase = G * mass1 * mass2 / radius**2 #1 вариант решения
forceSndCase = (G * mass1 * mass2) / (radius * radius) #2 вариант решения

print(forceFstCase)
print(forceSndCase)