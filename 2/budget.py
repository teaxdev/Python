# 2.6 Python budget calculator practice

# ask user for their budget for the month
total_budget = input("What is your total budget? (total monthly income) ")
total_budget = int(total_budget)

# ask user for their budget for their needs
housing_budget = input("What is your housing budget? (rent or mortgage) ")
housing_budget = int(housing_budget)

utilities_budget = input("What is your utilities budget? ")
utilities_budget = int(utilities_budget)

groceries_budget = input("What is your groceries budget? ")
groceries_budget = int(utilities_budget)

transport_budget = input("What is your transportation budget? ")
transport_budget = int(transport_budget)

healthcare_budget = input("What is your healthcare budget? ")
healthcare_budget = int(healthcare_budget)

personal_budget = input("What is your personal budget? ")
personal_budget = int(personal_budget)

clothing_budget = input("What is your clothing budget? ")
clothing_budget = int(clothing_budget)

debt_budget = input("What is your debt budget? ")
debt_budget = int(clothing_budget)

# calc calculates the the percentages for each category -
# represented by the initial 

hou_budget = housing_budget / total_budget * 100
# also use the round function to round when numbers are uneven
hou_budget = round(hou_budget, 1)

u_budget = utilities_budget / total_budget * 100
u_budget = round(u_budget, 1)

g_budget = groceries_budget / total_budget * 100
g_budget = round(g_budget, 1)

t_budget = transport_budget / total_budget * 100
t_budget = round(t_budget, 1)

he_budget = healthcare_budget / total_budget * 100
he_budget = round(he_budget, 1)

p_budget = personal_budget / total_budget * 100
p_budget = round(p_budget, 1)

c_budget = clothing_budget / total_budget * 100
c_budget = round(c_budget, 1)

d_budget = debt_budget / total_budget * 100
d_budget = round(d_budget, 1)

# print message to see whether you are within budget
if total_budget >= hou_budget + u_budget + g_budget + t_budget + he_budget + p_budget + c_budget + d_budget:
    print("congratulations! you are within your budget!")

else: print("oh no, looks like you are currently outside you budget.")

# print results
print(f"Your percentage for your housing budget is {hou_budget}%")
print(f"Your percentage for your utilities budget is {u_budget}%")
print(f"Your percentage for your groceries budget is {g_budget}%")
print(f"Your percentage for your transportation budget is {t_budget}%")
print(f"Your percentage for your healthcare budget is {he_budget}%")
print(f"Your percentage for your personal budget is {p_budget}%")
print(f"Your percentage for your clothing budget is {c_budget}%")
print(f"Your percentage for your debt budget is {d_budget}%")
