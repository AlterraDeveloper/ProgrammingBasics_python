# Составьте программу fiveperline . ру, использующую один цикл for и один оператор i f для вывода, 
# по пять в строку, целые числа от 1 ООО (включи­тельно) до 2 ООО (исключительно). 
# Подсказка: используйте оператор%. 

for i in range(1000, 2000):
    print(i, end=' ')
    if i % 5 == 4:
        print()
