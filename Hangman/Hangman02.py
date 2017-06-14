"""
A simple Hangman game
https://en.wikipedia.org/wiki/Hangman_(game)
Hangman is a paper and pencil guessing game of two or more players.
One player thinks of a word, phrase or sentence and the other tries
to guess it by suggesting letters or numbers, within a certain number of guesses.
"""

import sys
import random

def main():
    print(
        "Welcome to Hangman! A word will be chosen at random and",
        "you must try to guess the word correctly letter by letter",
        "before you run out of attempts. Good luck!",
        sep="\n"
        )

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        # Unixwords is simply a newline-delimited list of dictionary words.
        # rstrip("\n") rstrip lets you pass in what characters you want to remove from the end of a string.
        chosen_word = random.choice(open("Unixwords").readlines()).lower().rstrip("\n")
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        randomNumber = random.randrange(len(chosen_word))
        word_guessed[randomNumber] = chosen_word[randomNumber] # give a hint character
        joined_word = None # joins the words in the list word_guessed

        HANGMAN = (
            "--------\n|   |\n|\n|\n|\n|\n|\n|\n|\n--------",
            "--------\n|   |\n|   0\n|\n|\n|\n|\n|\n|\n--------",
            "--------\n|   |\n|   0\n|  -+-\n|\n|\n|\n|\n|\n--------",
            "--------\n|   |\n|   0\n| /-+-\n|\n|\n|\n|\n|\n--------",
            "--------\n|   |\n|   0\n| /-+-\ \n|\n|\n|\n|\n|\n--------",
            "--------\n|   |\n|   0\n| /-+-\ \n|   |\n|\n|\n|\n|\n--------",
            "--------\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|\n|\n|--------",
            "--------\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |\n|\n|\n--------",
            "--------\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |\n|  |\n|\n--------",
            "--------\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  | |\n|  |\n|\n--------",
            "--------\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  | |\n|  | |\n|\n--------"
        )

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1

        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(("The letter : {}").format(joined_word))
            print(("You have guess letter : {}").format(guessed_letters))
            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except KeyboardInterrupt:
                print("Ok ok, quitting")
                sys.exit(1)
            except EOFError: # Ctrl+D will cause EOFError exception
                sys.exit(0)
            except: # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: # check the input is only one letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for idx, letter in enumerate(chosen_word):
                if player_guess == letter:
                    word_guessed[idx] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again? [Y/N]\n")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()

"""
To-Do:
    Add translate
    http://pythonhosted.org/goslate/

"""
