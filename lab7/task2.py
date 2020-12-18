import functools 

people = [{'имя': 'Маша', 'рост': 160},
{'рост': 'Саша', 'рост': 80},
{'name': 'Паша'}]

height_total = 0
height_count = 0

for person in people:
    if 'рост' in person:
        height_total += person['рост']
        height_count += 1
    if height_count > 0:
        average_height = height_total / height_count
print(average_height) # => 120

people2 = [{'имя': 'Маша', 'рост': 160},
{'рост': 'Саша', 'рост': 80},
{'name': 'Паша'}]

filteredPeople = filter(lambda person: 'рост' in person, people2)
mappedPeople = map(lambda person: person['рост'], filteredPeople)
average_height = functools.reduce(lambda a, b: a + b, mappedPeople) / len(list(filter(lambda person: 'рост' in person, people2)))
print(average_height) # => 120






