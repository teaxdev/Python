"""
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word
- Change the word list to 15 words on a subject of your choice
"""

import random

WORD_LIST = ("PYTHON", "COBOL", "JAVASCRIPT", "BASIC")


def game(answer, display):
    wrong = 0
    right = 0

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")

    guessed_letters = []  # You will add logic to use this

    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        # TODO: Before checking if the letter is in the word,
        # check if the letter is already in guessed_letters
        # If it is, print a message like "You already guessed that letter!" and skip the rest of the loop
        # If not, add it to guessed_letters

        bad_guess = True
        for index, letter in enumerate(answer):
        for letter in range(len(answer)):
            if guess == answer[letter]:
                display[letter] = guess
                right += 1
                bad_guess = False

        if bad_guess:
            print("Wrong!")
            wrong += 1
            if wrong > 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if right == len(answer):
            print("You Win!")
            print("The word was:", answer)
            break


def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()
