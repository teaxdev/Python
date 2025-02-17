# 3.3 logical operations homework

# prompt = int(input("Enter an integer that will represent A: "))
# prompt2 = int(input("Enter an integer that will represent B: "))

prompt = 6

for i in range(1, prompt):
    if i / prompt != 1:
        continue
    if 1 / prompt == 2:
        print("A is a prime number")
    else:
        print("A is not a prime number")
