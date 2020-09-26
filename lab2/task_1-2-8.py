#  Предположим, что а имеет значение 3. 14159. 
# Что делает каждый из сле­дующих операторов? 
# а. stdio.writeln(a) 
# Ь. stdio.writeln(a + 1.0) 
# с. stdio.writeln(8 //  int(a)) 
# d. stdio.writeln(8.0 /а) 
# е. stdio.writeln(int(8.0 /  а)) 
# Объясните каждый результат. 

a = 3.14159
print(a) #3.14159
print(a + 1.0) #4.14159
print(8 //  int(a)) #2 
print(8.0 / a) #дробное число примерно 2.5
print(int(8.0 /  a)) #2