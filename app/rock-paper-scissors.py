# This is my rock paper scissors game 

print("Welcome to my game!")

player_choice = input("Please select an option from ('rock', 'paper', 'scissors'):")

import random

choice=["rock", "paper", "scissors"]

computer_choice = random.choice(choice)

print("Computer choice:", computer_choice)

if player_choice=='rock' and computer_choice=='paper':
    print("Sorry, computer won this round. Please try again!")
elif player_choice=='rock' and computer_choice=='scissors':
    print("Congratulations! You won this round!")
elif player_choice=='paper' and computer_choice=='rock':
    print("Congratulations! You won this round!")
elif player_choice=='paper' and computer_choice=='scissors':
    print("Sorry, computer won this round. Please try again!")
elif player_choice=='scissors' and computer_choice=='paper':
    print("Congratulations! You won this round!")
elif player_choice=='scissors' and computer_choice=='rock':
    print("Sorry, computer won this round. Please try again!")
else:
    print("This round was a tie. Please try again!")