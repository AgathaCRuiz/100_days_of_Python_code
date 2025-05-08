def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
        return True
    else:
        print(f"{year} is not a leap year.")
        return False

year = 2024
is_leap_year(year)
