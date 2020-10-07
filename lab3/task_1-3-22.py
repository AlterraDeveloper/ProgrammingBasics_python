# Составьте программу gamblerplot . ру, отслеживающую модель разоре­ния игрока, 
# выводя строки после каждой ставки, где одна звездочка со­ответствует каждой фишке, принадлежащей игроку. 

import random 
import sys 

stake = int(sys.argv[1]) 
goal = int(sys.argv[2]) 
trials = int(sys.argv[3])

bets = 0 
wins = 0 
chip_nominal = 5 #сколько баксов стоит одна фишка

for _ in range(trials):  
    # Запуск одной попытки. 
    cash = stake 
    while  (cash > 0)  and (cash < goal ): 
        #  Модель одной ставки. 
        bets +=  1 
        if random.randrange(0, 2) ==  0: 
            cash += chip_nominal 
        else : 
            cash -= chip_nominal
        line = ''
        for i in range(cash//chip_nominal): line += '*'
        print(line) 
    if cash == goal: 
        wins += 1

print(str( 100 * wins  //  trials) + '% wins') 
print( 'Avg а bets: ' + str(bets  //  trials)) 