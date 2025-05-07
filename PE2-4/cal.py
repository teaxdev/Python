# 4.6 Calendar and datetime modules
import calendar
import datetime


def main():
    datetime.datetime.now().year
    birth_month = int(input("What is your birth month? (1-12): "))
    if birth_month > 12 or birth_month < 0:
        print("Please enter a number 1-12!")
        main()
    else:
        print(calendar.month(2025, birth_month))
        # cal = calendar.Calendar()
        # for day in cal.itermonthdays(2024, birth_month):
        #     print(day)

# on a side note, naming your file calendar.py breaks every calendar module
# I'm not sure if you ever mentioned that, if not it would be nice to add a note on the assignment page


main()
