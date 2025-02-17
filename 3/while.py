# 3.2 while loop homework

count = 3
bottle = "bottles"

while count > 0:
    print(f"{count} " + bottle + " of beer on the wall")
    print(f"{count} " + bottle + " of beer")
    if count > 1:
        print("Take one down, pass it around")
    count -= 1
    if count == 1:
        bottle = "bottle"
    if count > 0:
        print(f"{count} " + bottle + " of beer on the wall!")
        print("")
    else:
        print("Take it down, pass it around")
        print("No bottles of beer on the wall!")
        break

#    elif count == 0:
#        bottle = "bottles"
# else:
#        print("Take it down, pass it around")
#        print("No bottles of beer on the wall!")
