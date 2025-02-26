# 3.7 python homework: define time_slots with a list of times of day, create a loop to prompt user for
# heart rate for each time slot. Create a multi level list called heart_rates to store in time slots
# with corresponding heart rates. Then calculate heart rate and display it.

time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
grammar = "in the"

for i in range(len(time_slots)):
    if i == 1:
        grammar = "at"
    else:
        grammar = "in the"
    heart_rates.append(int(input(
        f"What is your heart rate (in BPM) {grammar} {time_slots[i]}?: ")))
    i += 1
print(heart_rates)
