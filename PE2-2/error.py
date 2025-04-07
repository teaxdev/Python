# PE2 Module 2.6

import random

gen_random = random.randrange(1, 50)


def intro():
    print("Welcome to the number guessing game!")
    print("What is your name?")
    try:
        name = input(str("Your name: "))
    except ValueError:
        print("I don't think you're a robot, please enter your name!")
    print(f"Alright {name}, you're going to guess a number between 1-50!")
    print("You get 5 tries!")


def main():
    intro()
    try:
        input("Please set your initial guess!: ")
    except ValueError:
        print("Please enter a number from 1-50!")


main()
