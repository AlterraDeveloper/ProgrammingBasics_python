# Составьте версию gambler.ру, который использует два вложенных цикла while или 
# два вложенных цикла while вместо цикла while в цикле for. 

import random 
import sys 

stake = int(sys.argv[1]) 
goal = int(sys.argv[2]) 
trials = int(sys.argv[3]) 

bets = 0 
wins = 0 
trial = 1

while trial <= trials:  
    # Запуск одной попытки. 
    cash = stake 
    while  (cash > 0)  and (cash < goal ): 
        #  Модель одной ставки. 
        bets +=  1 
        if random.randrange(0, 2) ==  0: 
            cash += 1 
        else : 
            cash -=1 
    if cash == goal: 
        wins += 1
    trial += 1
        
print(str( 100 * wins  //  trials) + '% wins') 
print( 'Avg а bets: ' + str(bets  //  trials)) 