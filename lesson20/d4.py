# # d4 - ex 2
# def filter_out_vowels(word: str) -> str:
#     return "".join(filter(lambda c: c not in "aAeEiIoOuU", word))
#
#
# if __name__ == '__main__':
#     print(filter_out_vowels('The Sun is shining'))


# d4 - ex 3
from datetime import datetime


def filter_dates(dates_list):

    dates_mapping = map(lambda date_str: datetime.strptime(date_str, "%d-%m-%Y"), dates_list)

    #option 1
    # filtered_dates = filter(lambda date_obj: date_obj.weekday() not in (4, 5), dates_mapping)

    # option 2
    filtered_dates = filter(lambda date_obj: date_obj.strftime("%a") not in ("fri", "sat"), dates_mapping)
    return list(filtered_dates)


# def sort_strings_by_len(strs_list: list[str]) -> list[str]:
#     return list(sorted(strs_list, key=len))
#
#
# if __name__ == '__main__':
#     print(sort_strings_by_len(['clouds', 'sun', 'weather', 'rain', 'snow', 'heat', 'freeze']))

if __name__ == '__main__':
    print(filter_dates(['12-12-2021', '18-12-2021', '19-12-2021']))
