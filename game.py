import random as r
import sys


def pick_diff():
    """Allow the player to pick a difficulty."""
    print(name + ", choose between three difficulties."
          "\nEasy: between 1-10 with 3 incorrect guesses."
          "\nMedium: between 1-20 with 4 incorrect guesses."
          "\nHard: between 1-40 with 5 incorrect guesses."
          )
    choice = input("[E/M/H]\n> ").lower()
    while choice not in ['e', 'm', 'h']:
        choice = input("Pick a valid difficulty. [E/M/H]\n> ").lower()
    else:
        random_number(choice)


def random_number(diff):
    """Generate random number and assign incorrect guess attempts."""
    if diff == 'e':
        b = 10
        attempts = 3
    if diff == 'm':
        b = 20
        attempts = 4
    if diff == 'h':
        b = 40
        attempts = 5
    num = r.randint(1, b)
    play_game(num, attempts)


def play_game(n, a):
    """Play the game."""
    numb = n
    chances = a
    while chances > 0:
        print("\nYou have " + str(chances) + " guesses left.")
        guess = input("Guess a number: ")
        guess = int(guess)
        if guess == numb:
            print("\n\nCONGRATULATIONS, YOU WON!!\n\n")
            play_again()
        else:
            chances -= 1
            if guess > numb:
                print("\nYour guess was too high.")
            else:
                print("\nYour guess was too low.")
    else:
        print("Your number was " + str(numb) + ".")
        play_again()


def play_again():
    """Offer the chance to play again."""
    repeat = input("Would you like to play again? [Y/N]\n> ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("[Y/N]\n> ").lower()
    else:
        if repeat == 'y':
            pick_diff()
        else:
            print("Thanks for playing! See you next time!")
            sys.exit()


name = input("Let's play a number guessing game."
             "Please enter your name.\n> "
             ).title()
pick_diff()
