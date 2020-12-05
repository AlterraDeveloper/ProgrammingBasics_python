# Составьте функцию majority( ), получающую три аргумента типа bool
# и возвращающую значение True, если по крайней мере два из аргументов
# True, и значение False в противном случае. Не используйте оператор if.
a = input('ВВедите значение а: ').lower() == 'true'
b = input('ВВедите значение b: ').lower() == 'true'
c = input('ВВедите значение c: ').lower() == 'true'


def majority(a,b,c):
    return ((a == True and b == True) or (a == True and c == True) or (b == True and c == True))
    
print(majority(a, b, c))