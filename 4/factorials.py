# 4.5 Factorials Homework: Define a function factorial that takes one parameter, n, that represents the
# number you're calculating for. In that function, define the base case: n == 1 or n == 0, where the factorial is 1
# return n * factorial(n-1) if n > 1. prompt the user for a non-negative integer, then call and print factorial.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return n * factorial(n - 1)
    else:
        print("Please enter a non-negative number!")


n = int(input("Please enter a non-negative number: "))
print(factorial(n))
