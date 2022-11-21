def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


# return amount of days in month and year
def get_days_in_month(month: int, year: int) -> int:
    if is_31_days_month(month):
        return 31
    elif month == 2:
        # return 29 if is_leap_year(year) else 28
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30


def is_31_days_month(month):
    return month in (1, 3 , 5, 7, 8, 10, 12)

y = int(input("year: "))
m = int(input("month: "))
days_num = get_days_in_month(m, y)
print("days in month: ", days_num)


