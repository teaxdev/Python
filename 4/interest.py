# 4.3 interest calculator: create and call a function named calculate_interest, take three parameters,
# principal, rate and time. use return to send the computed interest back to the main function.
# print the formatted strings in the main function.

# calc_interest calculates the users inputs and displays the results
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print(
        f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
    return interest


input_principal = int(input("What is your starting amount?: "))
input_rate = int(input("What is your interest rate?: "))
input_time = int(input("Enter the time in years: "))

# used to return the parameters back to the function
interest = calculate_interest(principal=input_principal,
                              rate=input_rate, time=input_time)
