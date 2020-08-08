# lets creat our pc by random
import random

# the moves that the pc can choose

moves = ["rock", "paper", "scissors"]

keep_playing = "true"

countC = 0
countP = 0
countT = 0

while keep_playing == "true":

    cmove = random.choice(moves)

    pmoves = input("what is your move: rock, paper or scissors ?")

    print("The computer choos", cmove)

    if cmove == pmoves:
        print("Tie")
        countT +=1

    elif pmoves == "rock" and cmove == "scissors":
        print("Player Wins!!")
        countP +=1
    elif pmoves == "rock" and cmove == "paper":
        print("Computer wins ): ")
        countC +=1

    elif pmoves == "paper" and cmove == "rock":
        print("Player Wins!!")
        countP +=1

    elif pmoves == "paper" and cmove == "scissors":
        print("Computer wins ): ")
        countC +=1

    elif pmoves == "scissors" and cmove == "paper":
        print("Player Wins!!")
        countP +=1

    elif pmoves == "scissors" and cmove == "rock":
        print("Computer wins ): ")
        countC +=1

    print("Computer won: ", countC)
    print("Player won: ", countP)
    print("Tie", countT)

    if countC == 3:
        print("The computer won ):")
        break
    elif countP == 3:
        print("Great job! you have won the game!!")
        break
# a counter for wins and tie

