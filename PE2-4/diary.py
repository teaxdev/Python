# PE2-4 4.2 Processing 

def main():
    print("Welcome to PyDiary!, please input your diary log")
    day = input("Date: ")
    time = input("Time: ")
    entry = input("Write diary entry: ")
    with open('Python/PE2-4/diary.txt', 'a') as file:
        file.write(f"{day}\n\n{time}\n\n{entry}\n\n")
        file.close()


main()