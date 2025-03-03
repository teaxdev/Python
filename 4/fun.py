# 4.1 functions homework: define 2 functions, square and circle, where each function takes one parameter.
# calculate the area of the square and the circle, and test whether they display th correct values.

def square(side):  # the square function calculates the area and displays it
    s_calc = side * side
    print(f"The area of the square is {s_calc} square units")


square(4)


def circle(radius):  # the circle function calculates the area of the circle and displays it
    c_calc = 3.14 * radius * radius
    print(f"The area of the circle is {c_calc} square units")


circle(5)
