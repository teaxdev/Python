# 3.5 bubble sort homework

list_name = []

name_count = 5
while name_count != 0:
    name = input("Please give me a name: ")
    list_name.append(name)
    name_count -= 1
list_name.sort()

print(list_name)
