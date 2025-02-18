# 3.3 logical operations homework

# prompt = int(input("Enter an integer that will represent A: "))
# prompt2 = int(input("Enter an integer that will represent B: "))

prompt = 5

for i in range(2, prompt):
    if prompt % i == 0:
        print("A is not a prime number")
        break
    else:
        print("A is a prime number")
        break
