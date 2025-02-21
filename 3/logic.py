# 3.3 logical operations homework.

# prompt = int(input("Enter an integer that will represent A: "))
# prompt2 = int(input("Enter an integer that will represent B: "))

prompt = 42
prompt2 = 42

prime_a = False
prime_b = False

for i in range(2, prompt):
    if prompt % i == 0:
        # print("A is not a prime number")
        break
    else:
        # print("A is a prime number")
        prime_a = True
        break

for i in range(2, prompt2):
    if prompt2 % i == 0:
        # print("B is not a prime number")
        break
    else:
        # print("B is a prime number")
        prime_b = True
        break

if prime_b == True and prime_a == True:
    print("Both are prime numbers: True")
else:
    print("Both are prime numbers: False")

if prompt == 42 and prompt2 == 42:
    print("Both numbers are equal to 42: True, universe is safe")
else:
    print("Both numbers are equal to 42: False")

if prompt or prompt2 < 100:
    print("Either is less than 100: True")
else:
    print("Either is less than 100: False")

if prompt or prompt2 > 10:
    print("Either is greater than 10: True")
else:
    print("Either is greater than 10: False")

if not prompt / 2:
    print("A is not even: False")
else:
    print("A is not even: True")

if not prompt2 / 2:
    print("B is not odd: True")
else:
    print("B is not odd: False")
