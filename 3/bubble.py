# 3.5 bubble sort homework: prompt user for 5 list_name, store them in a list, sort them with bubble sort
# reverse the list, then print it

list_name = []

name_count = 5

while name_count != 0: # while loop that asks the user for input 5 times and adds them to a list
    name = input("Please give me a name: ")
    list_name.append(name)
    name_count -= 1
    
swapped = True
while swapped: # bubble sort to get the names sorted alphabetically
    swapped = False
    for i in range(len(list_name) - 1):
        if list_name[i] > list_name[i + 1]:
            list_name[i], list_name[i + 1] = list_name[i + 1], list_name[i]
            swapped = True

print(list_name)

list_name.reverse() # reverses the list

print(list_name)
