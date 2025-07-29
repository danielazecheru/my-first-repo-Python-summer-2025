# This is my rock paper scissors game 

print("Welcome to my game!")

player_choice = input("Please select an option from ('rock', 'paper', 'scissors'):")

import random

choice=["rock", "paper", "scissors"]

computer_choice = random.choice(choice)

print("Computer choice:", computer_choice)

def determine_winner(player_choice, computer_choice):
    if player_choice=='rock' and computer_choice=='paper':
        result = "COMPUTER WINS"
    elif player_choice=='rock' and computer_choice=='scissors':
        result = "PLAYER WINS"
    elif player_choice=='paper' and computer_choice=='rock':
        result = "PLAYER WINS"
    elif player_choice=='paper' and computer_choice=='scissors':
        result = "COMPUTER WINS"
    elif player_choice=='scissors' and computer_choice=='paper':
        result = "PLAYER WINS"
    elif player_choice=='scissors' and computer_choice=='rock':
        result = "COMPUTER WINS"
    else:
        result = "TIE"
    return result

print(determine_winner(player_choice, computer_choice))