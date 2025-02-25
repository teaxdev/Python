# 3.6 seats homework: create a list with seats from 1-20, display the seats to the customer then 
# ask them to select a seat and remove it after it is chosen. Display an updated list of available seats.
# when an invalid seat is chosen display an error message and prompt the user to try again.

seat_list = list(range(1, 21))
banned = []

print(seat_list)
print("You can press 0 to exit!")
while seat_list != 0:
    prompt = int(input("Choose a seat from 1 through 20, that wasn't chosen already, to be your seat!: "))
    if prompt == 0:
        break
    if prompt not in seat_list: # check if seat is in the list
        print("That is not a valid seat choice, please choose a different seat.")
    else:
        seat_list.remove(prompt)
        banned.append(prompt)
        print(prompt)
    print(seat_list)
    print(f"Used Seats: {banned}")