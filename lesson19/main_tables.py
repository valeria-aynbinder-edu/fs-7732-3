from lesson19.table_exceptions import *
from lesson19.table_system import Table

if __name__ == '__main__':
    # table1 = Table(1, 5)
    table2 = Table(2, 2)
    while True:
        try:
            # guests1 = int(input("insert_guests_num for table 1: "))
            # table1.reserve(guests1)
            guests2 = int(input("insert_guests_num for table 2: "))
            table2.reserve(guests2)
            print("Reserved")
            break
        except TableAlreadyReserved as e:
            print("You cannot reserve this table, it's occupied")
            break
        except InvalidGuestsNum as e:
            print(f"You inserted too many guests ({e.received_guests_num})"
                  f"This table can accomodate up to {e.table_guests_num} gueests")
        except ValueError as e:
            print("You did ont insert a number")
            continue
        except Exception as e:
            print("Unexpected error occurred")

