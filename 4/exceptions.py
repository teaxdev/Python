# 4.7 exceptions homework: Review the provided Python script, and consider errors that could be made
# with non numeric input. Implement blocks to catch a value error.

def square_number():
    number = input("Enter a number to square: ")
    try:
        number = int("abra cadabra")
    except ValueError:
        print("Error: Please enter a numeric value")
    else:
        print("squaring successful...")
    finally:
        print("EXECUTION SUCCESSFUL")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")


square_number()
