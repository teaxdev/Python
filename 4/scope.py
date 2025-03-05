# Create global variables for conversions for weight and height. Prompt the user for weight in pounds
# and height in inches. convert into metric units with the global conversion units. calculate BMI,
# determine BMI based on standard ranges, then display the value and category

# values to convert weight to kg and height to m
WEIGHT_CONVERSION = 0.453592
HEIGHT_CONVERSION = 0.0254

# function that takes weight and height, converts them, then prints bmi and weight category.


def calculate_bmi():
    weight = int(input("What is your weight in pounds: "))
    height = int(input("What is your height in inches: "))
    weight = weight * WEIGHT_CONVERSION
    height = height * HEIGHT_CONVERSION
    bmi = weight / (height * height)
    print(f"Your BMI is: {bmi:,.2f}")
    if bmi < 18.5:
        print("You are in the underweight category")
    elif bmi >= 18.5 < 25:
        print("You are in the normal weight category")
    elif bmi >= 25 < 30:
        print("You are in the overweight category")
    else:
        print("You are in the obese category")


calculate_bmi()
