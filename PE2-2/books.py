books = []


def main():
    while range(books) < 10:
        add_book = input("Please enter a book title: ")
        books.append(add_book)
    if len(books) == 10:
        sort()


main()

books_sorted = []


def sort():
