# 3.7 python homework: define time_slots with a list of times of day, create a loop to prompt user for
# heart rate for each time slot. Create a multi level list called heart_rates to store in time slots
# with corresponding heart rates. Then calculate heart rate and display it.

time_slots = ["Morning", "Midday", "Afternoon",
              "Evening"]  # defines the times of day
heart_rates = []  # creates an empty list that will have a nested list
rate_sum = []  # list that collects the heart rate to later get the average bpm
grammar = "in the"

# for loop that gets input on heart rate at different times of day.
for time in range(len(time_slots)):
    if time == 1:
        grammar = "at"
    else:
        grammar = "in the"
    rate = int(input(
        f"What is your heart rate (in BPM) {grammar} {time_slots[time]}?: "))
    heart_rates.append([time, rate])
    rate_sum.append(rate)
    time += 1

# sums up the heart rate to calculate the average on line 25
bpm_sum = sum(rate_sum)
bpm_average = float(bpm_sum / len(time_slots))

print(f"Your average heart rate today was: {bpm_average} BPM")
# print(heart_rates)
