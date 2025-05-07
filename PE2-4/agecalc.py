# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week

from datetime import datetime


def main():

    print("\n\n")
    try:
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(
            input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output)

        delta = today - birthday
        # Calculates the days, then divides by 30.5 to get months
        print(f'Difference is {delta.days / 30.5:.0f} months')
        # Calculates the days, then divides by 7 to get weeks
        print(f'Difference is {delta.days / 7:.0f} weeks')
        # Calculates days
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425

        print(f'You are {delta_years:.0f} years old')

    except Exception as e:
        print(f"ooooops!!!:  {e}")
        main()


main()
