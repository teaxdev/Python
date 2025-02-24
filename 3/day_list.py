# 3.4

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

steps = []

for i in range(len(days)):
    steps.append(int(input(f"How many steps did you take on {days[i]}? ")))
    i += 1
print(steps)
steps_sum = sum(steps)
print(f"Your total amount of steps: {steps_sum}")
steps_average = int(steps_sum / len(days))
print(f"Your average amount of steps: {steps_average}")
