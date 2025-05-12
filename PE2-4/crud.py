"""
CRUD - Start - students will finish on their own 
"""


def main_menu():
    try:
        print("\n                                         Menu              ")
        while True:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries")
            print("1. Create a new entry.")
            print("2. Display an entry by last name.")
            print("3. Update an existing entry. ")
            print("4. Remove an entry.")
            print("5. Quit")

            choice = int(
                input("Please enter the number of your selection:   "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That number is not valid. Please try again.")
    except ValueError:
        print("That is not a valid entry, try again")
    except Exception as e:
        print(f"There was an error: {e}")


def check():
    # check for existence of data file, read records into list
    try:
        file = open("Python/PE2-4/customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("\nCustomer list does not exist. Creating new customer database....")
        return []


def create():
    # create a new record
    customers = check()
    fname = input("Please enter the customer\'s first name:  ")
    lname = input("Please enter the customer\'s last name:  ")
    phone = input("Please enter the customer\'s phone number:  ")
    email = input("Please enter the customer\'s email:  ")
    entry = f"{fname}, {lname}, {phone}, {email}"
    print(entry)  # for test purposes
    customers.append(entry)
    print(customers)
    save(customers)


def read():
    # read a record - used by delete and update
    print("Read")
    try:
        customers = check()

        search_records = input("Enter the name of the customer: ")

        for c in customers:
            print(f"searching customers: {c}")
            if search_records in c:
                print("Customer Found\n")
                c_index = customers.index(c)
                return c, c_index
            
        else:
            print("Customer does not exist!")

    except Exception as e:
        print(f"READ: {e}")

    main()


def update():
    
    try:
        output, c_index= read()
        entry = output.split(", ")
        lname = entry[0]
        fname = entry[1]
        phone = entry[2]
        email = entry[3]
        print("1: " + lname + "\n2: " + fname + "\n3: " + phone + "\n4: " + email )
        choice  = int(input("Enter the number of the value that you want to change: "))
        if choice == 1:
            lname = input("Please enter a new last name: ")
        elif choice == 2:
            fname = input("Please enter a new first name: ")
        elif choice == 3: 
            phone = input("Please enter a new phone number: ")
        elif choice == 4: 
            email = input("please enter a new email:  ")
    
        # delete old record
        customer = check()
        del customer[c_index]

        # add new record
        entry = (fname + ", " + lname + ", " + phone + ", "  + email + "\n")
        customer.append(entry)
        save(customer)
    
    except Exception as e:
        print(f"Update problem! {e}")

    main()

    print("Update")


def delete():
    # removes a record
    try:
        customer = check()
        print("Searching for the record you would like to delete. ")
        output, c_index = read()
        print(output)
        confirm = input("Would you like to delete this record? (y/n)  ")
        if confirm.lower() == 'y':
            print("deleting")
            del customer[c_index]
        else:
            print("File has not been deleted (Output other than 'y'). ")
    except Exception as e:
        print(f"Error deleting: {e}")
    
    main()
    print("Delete")


def save(customers):
    # Save the current list into the text file
    file = open("customer_list.txt", 'w')
    for line in customers:
        file.write(line)
    file.close()
    print("customer database updated.")


def main():
    choice = main_menu()
    if choice is None:
        choice = main_menu()
    elif choice == 1:
        create()
        choice = main_menu()
    elif choice == 2:
        read()
        choice = main_menu()
    elif choice == 3:
        update()
        choice = main_menu()
    elif choice == 4:
        delete()
        choice = main_menu()
    elif choice == 5:
        print("Goodbye!")


main()
