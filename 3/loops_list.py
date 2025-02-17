'''
    While loops
    For Loops
    Lists

'''

# Flag demo
# entry = "hi"
# while entry != "done":
#     entry = input("How are you today? enter 'done' when finished. ")
#     if entry != "done":
#         print("it is one of those days, isn't it?")


# number = 10
# while number >= 0:
#     print(number)
#     number -= 1  # same as number = number -1

# for num in range(10, -1, -1):
#     if num == 5:
#         continue
#     if num == 3:
#         break
#     print(num)


# Lists

# jenny = [8, 6, 7, 5, 3, 0, 9]
# print(f"initial list {jenny}.")
# jenny.append(12)
# print(f"New list after appending 12: {jenny}")


# my_index = 0
# for num in jenny:
#     jenny[my_index] = num + 2
#     my_index += 1  # my_index = my_index + 1
# print(f"The new list: {jenny}")

days_of_week = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]

print(days_of_week)
days_of_week.sort()
print(days_of_week)
days_of_week.reverse()
print(days_of_week)

# days_of_week.append("Sunday")
# print(days_of_week)
# days_of_week.pop(2)
# days_of_week.remove("Sunday")
# print(days_of_week)


# for day in days_of_week:
#     print(day)


# print(f"There are {len(days_of_week)} days in a week")
