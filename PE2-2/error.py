# PE2 Module 2.6

import random

gen_random = random.randrange(1, 50)


print("Welcome to the number guessing game!")
print("What is your name?")
name = input("Your name: ")
print(f"Okay {name}, What difficulty would you like? (1 = Easy, 2 = Medium, 3 = Hard)")
try:
    challenge = int(input("Difficulty: "))
    if challenge == 1:
        diff = 10
    elif challenge == 2:
        diff = 7
    else:
        diff = 5
except ValueError:
    print("Please enter a valid difficulty! (1-3)")
else: 
    print(f"Alright {name}, you're going to guess a number between 1-50!")
finally:
    print(f"You get {diff} tries!")




def victory():
    print(f"Congratulations! you guessed {gen_random}, and were correct!")

def loss():
    print(f"Bummer! Looks like you didn't guess {gen_random}!")
    

def main():
    tries = 0
    while tries < diff:
        try:
            num = int(input("Please set your guess!: "))
            if num > gen_random:
                print("Lower!")
                tries += 1
            elif num < gen_random:
                print("Higher!")
                tries += 1
            else:
                victory()
                break
        except ValueError:
            print("Please enter a valid number!")
       
    if tries > 7:
         loss()


main()
