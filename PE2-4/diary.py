# PE2-4 4.2 Processing 

def main():
    print("Welcome to PyDiary!, please input your diary log")
    # Get input for day, date and time
    day = input("Date: ")
    time = input("Time: ")
    entry = input("Write diary entry: ")
    #writes the inputs to the file, and creates the file if it doesn't exist
    with open('Python/PE2-4/diary.txt', 'a') as file:
        file.write(f"{day}\n\n{time}\n\n{entry}\n\n")
        file.close()


main()