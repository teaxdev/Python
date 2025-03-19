# PE2-1 1.1 and 1.2 homework: Create a list with 20 possible answers the could pertain to a magic 8 ball.
# Use the random module to select a random response every time the user asks a question.
# use a while loop to keep it going until the user decides to stop, by using a prompt.
# exit the loop if the user says no to the prompt

import random

response_list = ["Absolutely not.", "Please never ask that again.", "We both know that's not true.", "My friend, please seek help. This isn't okay.",
                 "Inquire your mother", "YES. Without a shadow of a doubt.", "If that isn't the right answer, I'm retiring.",
                 "Yes, but only if you eat a shawarma today.", "nah", "yea", "refer to the manual", "Based on Einstein's theory of relativity, I have no clue.",
                 "If that was true, I think I'd lose it.", "I dislike you as of this moment, ask me later", "After consulting my advisor, Sgt. Peanut, the answer is no.",
                 "If you think there's a chance that's true... I've got no words for you.", "I mean yes... but I don't like that",
                 "Of course!", "Ask me again in approximately 2 minutes and 18 seconds.", "They don't pay me enough for this $#!%- I'm out!"
                 ]


def greeting():
    print("Welcome to the thunderdome of truth traveler! The great Magic of the Eighth ball shall guide you.")
    input("Please, ask the almighty ball a yes or no question!: ")


def cont():
    loop = True
    print("Such wise words... would you like to continue?")
    respond = input("(Yay/Nay): ").lower()
    if respond == "nay":
        loop == False

    while loop == True:
        if respond == "yay":
            main()
        else:
            print("That is not a valid response, traveler. Please respond accordingly")
            cont()


def main():
    rand = random.randint(1, 20)
    greeting()
    print(f"The ball responds... {response_list[rand]}")
    if rand == 20:
        print("There he goes... came back again later.")
    else:
        cont()


main()
