# Aliabbas Syed [syeal01@hotmail.com]
# Play a random game with computer.

import random
import colorama

def play_game(random_number):
    count = 0
    guess = None
    print(random_number)
    while guess != random_number:
        guess = int(input(f"Guess number between 1 and 10: "))
        if random_number == guess:
            print(f"{guess} that's it. Guessed in {colorama.Fore.RED}{count}{colorama.Style.RESET_ALL} tries.")
        elif random_number > guess:
            print(f"Guess Number {colorama.Fore.RED}{count}{colorama.Style.RESET_ALL}: {guess} is too low. Guess again... ")
            count += 1
        elif random_number < guess:
            print(f"Guess Number {colorama.Fore.RED}{count}{colorama.Style.RESET_ALL}: {guess} is too high. Guess again... ")
            count += 1

play = 1
while play == 1:
    play_game(random.randint(1, 10))
    print("Play again? (y/n): ")
    play = input()
    play = 1 if play == 'y' else 0
