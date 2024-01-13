import random

def jogo():
    score1 = 0
    score2 = 0

    while True:
        print("menu:")
        print("1 - play")
        print("2 - exit")
        select = int(input("select a number:"))

        if select == 1:
            player1 = int(input(''' 
            player 1 turn.
            1 - rock
            2 - paper
            3 - scissor
            '''))
            player2 = int(input(''' 
            player 2 turn
            1 - rock
            2 - paper
            3 - scissor
            '''))
        if(player1 == 1 and player2 == 2):
            print("player 2 win.")
            score2 += 1

        if(player1 == 2 and player2 == 3):
            print("player 2 win.")
            score2 += 1
        
        if(player1 == 3 and player2 == 1):
            print("player 2 win.")
            score2 += 1
        
        if(player2 == 1 and player1 == 2):
            print("player 1 win.")
            score1 += 1

        if(player2 == 2 and player1 == 3):
            print("player 1 win.")
            score1 += 1
        
        if(player2 == 3 and player1 == 1):
            print("player 1 win.")
            score1 += 1

        if(player1 == 1 and player2 == 1):
            print("draw")

        if(player1 == 2 and player2 == 2):
            print("draw")

        if(player1 == 3 and player2 == 3):
            print("draw")
        
        print("end game, ranking")
        print(f"player 1: {score1} points")
        print(f"player 2: {score2} points")
        break

    else:
        print("error, try again.")

jogo()
