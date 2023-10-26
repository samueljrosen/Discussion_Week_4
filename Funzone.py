import random 
#Stars: if number>0, loop from 1 to number and print a line with that amount of stars. Example output:
#stars(3)
#*
#**
#***

#Fix this code to make sure it fails for number<=0. Write an AssertionError for if number<=0
def stars(number):
    for i in range(1,number):
        print(number*'*')
        
#Rock_paper_scissors: move needs to be 'Rock', 'Paper', 'Scissors'. Program follows standard rock paper scissors rules. 
#Example output:
#Win: rock_paper_scissors('Rock'): -> Rock beats Paper! You win!
#Lose: rock_paper_scissors('Rock'): -> Rock loses to Paper! You lose!
#Draw: rock_paper_scissors('Rock'): -> You tied! Oh well!
#Include an AssertionError for a wrong input. 
def rock_paper_scissors(move):
    rand_move = str(random.randint(1,3))
    ENEMY_MOVE_LIST = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}
    ENEMY_MOVE = ENEMY_MOVE_LIST[rand_move]
    WINNING_COMBOS = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper' }
    if WINNING_COMBOS[move]==ENEMY_MOVE:
        print(move, ' beats', ENEMY_MOVE, '! You win!')
    ##Write code for what happens if the player loses
    
    ##Write code for what happens if the player and enemy tie 
    

    
    