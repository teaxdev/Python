# 4.7 exceptions homework: Review the provided Python script, and consider errors that could be made
# with non numeric input. Implement blocks to catch a value error.

def square_number():
    number = input("Enter a number to square: ")
    try:
        squared_number = int(number) ** 2
    except ValueError:
        print("Error: Please enter a numeric value")
    else:
        print("squaring successful...")
        print(f"The square of {number} is {squared_number}.")
    finally:
        print("EXECUTION SUCCESSFUL")


square_number()
