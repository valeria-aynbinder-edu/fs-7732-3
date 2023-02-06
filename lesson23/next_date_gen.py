import datetime


def nex_date_gen(init_date=datetime.date.today()):
    next_day = init_date
    while next_day.month == init_date.month:
        yield next_day
        next_day = next_day + datetime.timedelta(days=1)


if __name__ == '__main__':
    # for i in nex_date_gen(datetime.date(2023, 1, 3)):
    #     print(i)
    for i in nex_date_gen():
        print(i)