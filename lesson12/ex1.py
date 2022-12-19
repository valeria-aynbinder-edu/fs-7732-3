import datetime


def get_date_in_3_days(original_date: str):
    dt = datetime.datetime.strptime(original_date, "%Y-%m-%d, %a, %H:%M")
    new_dt = dt + datetime.timedelta(days=3)
    return new_dt.strftime("%A")


if __name__ == '__main__':
    print(get_date_in_3_days('2022-12-19, Mon, 19:00'))