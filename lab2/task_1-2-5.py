# Что делает каждый из операторов? 
# а. stdio.writeln(2 +  3) 
# Ь. stdio.writeln(2.2  +   3.3) 
# с. stdio.writeln( '2' +  '3') 
# d. stdio.writeln( '2.2' + '3.3') 
# е. stdio.writeln(str(2) +  str(3)) 
# f. stdio.writeln(str(2.2) +  str(3.3)) 
# g. stdio.writeln(int('2') + int('3' )) 
# h. stdio.writeln(int('2' + '3')) 
# i. stdio.writeln(float( '2')  +   float( '3' )) 
# j. stdio.writeln(float( '2' +  '3' )) 
# k. stdio.writeln(int(2.6 + 2.6)) l. stdio. writeln(int(2 6) +  int(2.6)) 
# Объясните каждый результат. 


print(2 +  3) #5
print(2.2  +   3.3) #5.5 
print( '2' +  '3') #23
print( '2.2' + '3.3') #2.23.3
print(str(2) +  str(3)) #23
print(str(2.2) +  str(3.3)) #2.23.3
print(int('2') + int('3')) #5 
print(int('2' + '3')) #23
print(float( '2')  +   float( '3' )) #5.0 
print(float( '2' +  '3' )) #23.0
print(int(2.6 + 2.6))  #5
print(int(2.6) +  int(2.6)) #4 