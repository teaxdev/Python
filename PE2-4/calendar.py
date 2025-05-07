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



main()