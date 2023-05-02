import random

def get_choices():
    i = 0
    player_choice = input("Enter a choice => rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    while player_choice != options[i]:
        player_choice = input("Wrong input, Try again => rock, paper, scissors: ")
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice} 
    return choices






def check_win(player, computer):
    print(f"You chose: {player} and computer chose: {computer}")
    if player == computer:
        return ("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!" 
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! YOu win"
        else:
            return "Scissors cuts paper. YOu lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!" 

choices = get_choices()
  
player = choices.get("player")
computer = choices.get("computer")

result = check_win(player, computer)
print(result)