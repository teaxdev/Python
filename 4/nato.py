# Python 4.6.B homework: NATO alphabet. Create a dictionary named nato_alphabet where each key is a letter,
# and has a corresponding NATO term according to its value. Write a function to prompt the user for a word
# and iterate through each letter and print the corresponding phonetic terms. Use a main function!

nato_alphabet = {"a": "Alpha", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo", "f": "Foxtrot", "g": "Golf",
                 "h": "Hotel", "i": "India", "j": "Juliet", "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November",
                 "o": "Oscar", "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango", "u": "Uniform",
                      "v": "Victor", "w": "Whiskey", "x": "X-ray", "y": "Yankee", "z": "Zulu"}


def main():
    inp = input("Please give me a word: ").lower()
    for i in inp:
        print(nato_alphabet[i])


main()
