# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# mapping numbers to theirs squares
def sq(x):
    return x**2
# equivalent
sq1 = lambda x: x**2

list(map(lambda x: x**2, [1,2,3,4]))

list(map(lambda x, y :x*y, [1, 3, 5], [2, 4, 6]))

# From buses - print only bus routes using lambda

print(list(map(lambda bus: bus['route_num'], buses_list)))

# Back to ex with dates - rewrite with lambdas

from datetime import datetime
def map_to_date(date_as_str):
    return datetime.strptime(date_as_str, "%d-%m-%Y")

def filter_days(date_obj):
    return date_obj.weekday() not in (4, 5)

print(list(filter(filter_days, map(map_to_date, ['12-12-2021', '18-12-2021', '19-12-2021']))))

print(
    list(
        filter(
            lambda date_obj: date_obj.weekday() not in (4, 5),
            map(
                lambda date_as_str: datetime.strptime(date_as_str, "%d-%m-%Y"),
                ['12-12-2021', '18-12-2021', '19-12-2021']
            )
        )
    )
)

# ex 4