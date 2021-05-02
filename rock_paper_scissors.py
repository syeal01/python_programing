# Aliabbas Syed (syeal01@hotmail.com)
# Rules of the Game
#    1. Rock breaks scissors.
#    2. Paper covers rock.
#    3. Scissors cut paper.

import random
import colorama
colorama.init()
game_choices = ["rock", "paper", "scissors"]
play_again = None

def play_hand():
    player_choice = input(f"Your hand {game_choices} as {colorama.Fore.RED}r/p/s {colorama.Style.RESET_ALL} (or q to quit): ")
    player_choice = player_choice.lower()
    if player_choice == "r": player_choice = game_choices[0]
    elif player_choice == "p": player_choice = game_choices[1]
    elif player_choice == "s": player_choice = game_choices[2]
    else: pass
    machine_choice = random.choice(game_choices)
    return(player_choice, machine_choice)

def computer_wins(): print(f"{colorama.Fore.RED}Computer Wins!{colorama.Style.RESET_ALL}")
def player_wins(): print(f"{colorama.Fore.GREEN}You win!{colorama.Style.RESET_ALL}")

def winner(player, machine):
    if player == machine: print(f"{colorama.Fore.YELLOW}It's a draw.{colorama.Style.RESET_ALL}")
    elif player == game_choices[0]:
        if machine == game_choices[1]: computer_wins()
        if machine == game_choices[2]: player_wins()
    elif player == game_choices[1]:
        if machine == game_choices[0]: player_wins()
        if machine == game_choices[2]: computer_wins()
    elif player == game_choices[2]:
        if machine == game_choices[0]: computer_wins()
        if machine == game_choices[1]: player_wins()
    else: print(f"Unhandled situation. Your hand must be {game_choices} as {colorama.Fore.RED}r/p/s {colorama.Style.RESET_ALL} (or q to quit): ")

while play_again != 'q':
    player, machine = play_hand()
    print(f"You: {player.upper()}. Computer: {machine.upper()}")
    winner(player, machine)

    play_again = player.lower()
