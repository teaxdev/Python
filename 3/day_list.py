# 3.4 Lists: create a list then a loop that asks for user input on steps taken on the respective day
# then provide the total amount of steps and the average steps every day

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

steps = []

for i in range(len(days)):
    steps.append(int(input(f"How many steps did you take on {days[i]}? ")))
    i += 1
print(steps)
steps_sum = sum(steps)  # use the sum function to add all step inputs
print(f"Your total amount of steps: {steps_sum}")
steps_average = int(steps_sum / len(days))
# takes the sum of the step inputs and divides it by the length of days
print(f"Your average amount of steps: {steps_average}")
