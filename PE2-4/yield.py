# 4.1 Generators, Iterators and Closures.
# You gave me permission to use different logic in class.

def two_letter_combo(letters):
    # For each letter, this loop adds the current letter, then uses yield to add each other letter in the list
    for x in letters:
        yield x + letters[0]
        yield x + letters[1]
        yield x + letters[2]
        yield x + letters[3]
        yield x + letters[4]


def main():
    # Calls the combination function and prints all possible combinations
    result = list(two_letter_combo(letters=['d', 'u', 'c', 'k', 'y']))
    print(result)


main()
