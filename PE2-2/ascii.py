"""
Start Your Python Script:
Open your Python environment and start a new script.
Use a main() function to organize your code.

Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:

Ensure the user enters precisely one character.
Use len() to check input length.

Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Example:
ascii_value = ord(user_input)
Display the Result:
Print the ASCII value to the user.

Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 32 and 127.
Use a try-except block to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
Example:
character = chr(ascii_input)
"""


def to_ascii():
    # Get and validate a single character from user
    # While - check length
    length = 2
    while length != 1:
        character = input("Please enter a single character:  ")
        length = len(character)
        if length == 0 or length > 1:
            print("Please enter a single character.")

    # convert to ASCII and Print
    ascii_value = ord(character)
    print(f"The ASCII value of {character} is {ascii_value}\n\n")


def from_ascii():

    # Get and validate number between 32 and 127
    # Try and except

    # convert frm ASCII and print
    print("from_ascii")


def greeting():
    print("Hello, welcome to the ASCII converter!")
    print("Would you like to: ")
    print(" 1. Convert from a character to ASCII")
    print(" 2. Convert from ASCII to a character")
    print(" 3. Quit")

    choice = int(input("Please enter a number between 1 and 3:  "))
    return (choice)


def main():

    choice = greeting()
    while True:
        if choice == 1:
            to_ascii()
            choice = greeting()
        elif choice == 2:
            from_ascii()
            choice = greeting()
        elif choice == 3:
            print("Goodbye")
            break
        else:
            print("\nI'm sorry that option isn't valid.")
            choice = greeting()


main()
