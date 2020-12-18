names = ['Маша', 'Петя', 'Вася']
names2 = ['Маша', 'Петя', 'Вася']
names3 = ['Маша', 'Петя', 'Вася']

#1
def hashName(name) : return hash(name)
names = map(hashName, names)
print(list(names))

#2
names2 = map(lambda name: hash(name), names2)
print(list(names2))

#3
for i in range(len(names3)):
    names3[i] = hash(names3[i])
print(names3)

