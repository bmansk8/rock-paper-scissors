from random import choice

choices = ["Rock", "Paper", "Scissors"]

outcomes = {
    "Rock": {
        "Rock": "tie",
        "Paper": "lose",
        "Scissors": "win"
    },
    "Paper": {
        "Rock": "win",
        "Paper": "tie",
        "Scissors": "lose"
    },
    "Scissors": {
        "Rock": "lose",
        "Paper": "win",
        "Scissors": "tie"
    }
}

def get_player_choice():
    while True:
        player = input("Rock, Paper, Scissors? \n").strip().capitalize()
        if player in choices:
            return player
        print("That's not a valid play. Please choose from Rock, Paper, or Scissors.")

def print_outcome(player_choice, computer_choice, result):
    if result == "win":
        print("You win! {} beats {}!".format(player_choice, computer_choice))
    elif result == "lose":
        print("You lose! {} loses to {}!".format(player_choice, computer_choice))
    else:
        print("That's a tie!")

def play_again():
    response = input("Do you want to play again? [Y/N] \n")
    return response.upper() == "Y"

def game_loop():
    while True:
        computer_choice = choice(choices)
        player_choice = get_player_choice()
        result = outcomes[player_choice][computer_choice]
        print_outcome(player_choice, computer_choice, result)
        if not play_again():
            break

game_loop()

__all__ = [game_loop, play_again, print_outcome, get_player_choice, outcomes, choices]