"""

Demo for 3.6 Operations on Lists

Requirements here
Understanding Python Lists: Key Concepts
Copying Lists: Assigning one list to another (e.g., new_list = my_list) creates a reference, not a new list. Changes to one list affect the other.
Correctly Copying a List: Use slicing to create a true copy: copied_list = my_list[:]. Changes to one list do not affect the other.
Using Slice for Partial Copy: Copy parts of a list with my_list[start:end], including the start index but excluding the end index.
Deleting List Elements with Slice: Remove elements with del, e.g., del my_list[2:6] removes elements from index 2 up to (but not including) index 6.
Checking for a Value: Use the in keyword to check if a value exists in a list, e.g., if value in my_list:.
List Operation Demos

"""

ages = []  # collect ages from user

# sort and do calculations
age = 99
print("Enter in ages. When you are done, type 0 to end data collection.")
while age != 0:
    age = int(
        input("Please enter the persons age as a whole number between 1 and 120:  "))
    if age < 0 or age > 120:
        print("That is not a valid age. ")
    if age != 0:
        ages.append(age)
    print(f"{ages} \n")

# Sort ages
sorted_ages = sorted(ages)  # copies and sorts

# copy
copied_ages = ages[:]

copied_ages = ages.copy()

# slice example
phone = [8, 6, 7, 5, 3, 0, 9]

jenny = phone[0:3]
print(f"Sliced: {jenny}")

if 3 in phone:
    print(f"3 is in phone")

if 2 in phone:
    print(f"2 is in phone")
else:
    print(f"2 is not in phone")


ages.sort()
print(f"Sorted: {ages} \n")

ages.reverse()
print(f"Reversed: {ages} \n")

total = sum(ages)
average = total / len(ages)

print(f"The average age is: {average:.1f}")

delinquent_accounts = [1056, 2008, 3278, 4189]
# Find the index of 2008 in the list
for i in range(len(delinquent_accounts)):
    if delinquent_accounts[i] == 2008:
        print("The account number 2008 is at index", i)

# For Loop Sample
# print("Enter in all ten of the ages as whole numbers between 1 and 120. Enter in 5 ages.")
# for i in range(1, 6):
#     age = int(
#         input("Please enter the persons age as a whole number between 1 and 120:  "))
#     if age < 0 or age > 120:
#         print("That is not a valid age. ")
#     if age != 0:
#         ages.append(age)
#     print(f"{ages} \n")
