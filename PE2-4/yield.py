# 4.1 Generators, Iterators and Closures.

def two_letter_combo():
    letters = ['a', 'b', 'c']
    for i in letters:
        yield i + letters 
        print(letters)

two_letter_combo()
# def main():


# main()
