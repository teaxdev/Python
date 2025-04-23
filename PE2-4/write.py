def main():
    try:
        students = []
        f_name = "Meri"
        print("Enter student names. Type 'Done' as first name to stop.")

        while f_name != "Done":
            f_name = input("First name: ").title()
            if f_name == "Done":
                break
            l_name = input("Last name: ").title()
            students.append(f_name + ', ' + l_name + '\n')

        my_file = open('reading_files/example.txt', 'w')
        for line in students:
            my_file.write(line)
        my_file.close()

        print("Students added:")
        print(students)

    except Exception as e:
        print("Error:", e)


main()
