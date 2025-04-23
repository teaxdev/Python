# 4.3 Working with files

def main():
    total = 0
    entries = 0
    try:
        with open('Python/PE2-4/reading_files/sales_totals.txt', 'r') as file:
            for line in file:
                line = line.strip('\n')
                print(line)
                total += float(line)
                entries += 1
            print(f"Total Sales: {total}")
            print(f"Number of entries: {entries}")
            average = total / entries
            print(f"Average: {average:.2f}")

    except IOError:
        print("IOError has occurred")


main()
