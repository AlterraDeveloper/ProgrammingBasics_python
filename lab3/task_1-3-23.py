# Измените программу gamЫe r. ру так, чтобы она получала дополнительный аргумент командной строки,  
# задающий (фиксированную) вероятность выигрыша при каждой ставке.  
# Используйте эту программу для проверки того, как эта вероятность влияет на шанс 
# достижения цели и количество ожидаемых ставок. Опробуйте значения, близкие к 0,5 (скажем, 0,48). 

import random 
import sys 

stake = int(sys.argv[1]) 
goal = int(sys.argv[2]) 
trials = int(sys.argv[3])
wins_probability = float(sys.argv[4])

bets = 0 
wins = 0 

for _ in range(trials):  
    # Запуск одной попытки. 
    cash = stake 
    while  (cash > 0)  and (cash < goal ): 
        #  Модель одной ставки. 
        bets +=  1 
        if random.randrange(0, 100) in range(int(wins_probability * 100)): 
            cash += 1
        else : 
            cash -= 1
    if cash == goal: 
        wins += 1

print(str( 100 * wins  //  trials) + '% wins') 
print( 'Avg а bets: ' + str(bets  //  trials)) 