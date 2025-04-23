#

def main():
    try:
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)
    except IOError:
        print("An IOError has occurred")

    # try:
    #     with open('example.txt', 'r') as file:
    #         line = file.readline()
    #         line = line.strip('\n')
    #     while line:
    #         print(line, end='')
    #         line = file.readline()
    #         line = line.strip('\n')
    # except IOError:
    #     print("An IOError has occurred.")

    # try:
    #     with open('example.txt', 'r') as file:
    #         lines = file.readlines()
    #     print(lines)
    # except IOError:
    #     print("An IOError has occurred.")


main()
