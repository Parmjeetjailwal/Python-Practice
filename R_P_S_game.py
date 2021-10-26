# Rock, Paper or Scissors Game

import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("It's a tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("Paper covers rock! You lose.")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("Rock smashes scissors! You win!")
            
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("Rock smashes scissors! You lose.")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("Scissors cuts paper! You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("Scissors cuts paper! You lose.")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("Paper covers rock! You win!") 

    play_again = input("Play again? (yes/no): ").lower()
    
    if play_again != "yes":
        break
    
    print("Bye!")