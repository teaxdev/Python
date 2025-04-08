# PE2-2 2.7-2.8 Anatomy of exceptions

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    print(top_artists)
    try:
        ind = int(input("Enter the index of the artist to replace: "))
        replace = input("Enter the new artist name: ")
        top_artists[ind] = replace
        print(f"Updated list: {top_artists}")
    except (IndexError, ValueError) as e: 
        print(f"An error occurred: {e}")


main()
    