# PE2-2 book sorting python homework

books = []
books_sorted = []

# sorting copies the books list and sorts it, then if there are 10 or more books, will print
# each title on a new line


def sorting():
    books_sorted = books.copy()
    books_sorted.sort()
    print("Here is a list of all of your books sorted!")
    if len(books_sorted) >= 10:
        for i in range(len(books_sorted)):
            print(books_sorted[i])
            i += 1

# main function collects 10 book titles and appends them to the books list


def main():
    print("Hello! Please give me 10 book titles!")
    while len(books) < 10:
        add_book = input("Please enter a book title: ")
        books.append(add_book)
    if len(books) == 10:
        sorting()


main()
