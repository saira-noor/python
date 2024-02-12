import random

choices = ["rock", "paper", "scissors"]

computer= random.choice(choices)



player = input("enter rock, paper or scissors: ")

print(f"computer chose {computer}")

if computer == player:
    print ("it's a tie!")
elif computer == "rock":
    if player == "paper":
        print("you win!")
    else:
        print("computer wins")

elif computer == "paper":
    if player == "scissors":
        print("you win!")
    else:
        print("computer wins")

elif computer == "scissors":
    if player == "rock":
        print("you win!")
    else:
        print("computer wins")
