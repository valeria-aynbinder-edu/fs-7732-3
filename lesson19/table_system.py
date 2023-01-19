import datetime
import os.path
import pickle

from lesson19.table_exceptions import *


class Table:

    def __init__(self, table_id, seats, max_time_limit=datetime.timedelta(minutes=90)):
        self.table_id = table_id
        self.seats = seats
        self.occupied_seats = 0
        self.start_time = None
        self.location = None
        self.max_time_limit = max_time_limit

    def is_available(self):
        return self.occupied_seats == 0

    def reserve(self, guests_num):

        # we allow to reserve a table only if it's available
        # and amount fo guests fits the amount of seats
        if self.occupied_seats != 0:
            raise TableAlreadyReserved()
        if self.seats < guests_num:
            raise InvalidGuestsNum(guests_num, self.seats)

        self.occupied_seats = guests_num
        self.start_time = datetime.datetime.utcnow()


    def release(self) -> bool:

        # The table is already available
        if self.occupied_seats == 0:
            return False

        self.occupied_seats = 0
        self.start_time = None

    def _get_end_time(self) -> datetime.datetime:
        return self.start_time + self.max_time_limit

    def time_left(self) -> datetime.timedelta:

        if not self.start_time:
            return datetime.timedelta()
        return self._get_end_time() - datetime.datetime.utcnow()

    def get_available_time(self) -> datetime.datetime:

        if not self.start_time:
            return datetime.datetime.utcnow()

        return self.start_time + self.max_time_limit

    def __str__(self):
        return f"Table id {self.table_id}, seats: {self.seats}, available: {self.is_available()}"

    def __repr__(self):
        return f"Table {self.table_id} ({self.seats})"


class TableReservationSystem:

    def __init__(self, tables_list: list, name: str, max_time_limit: datetime.timedelta=datetime.timedelta(minutes=90)):

        self.name = name
        self.max_time_limit = max_time_limit

        self.tables: list[Table] = []
        for i, table_seats in enumerate(tables_list):
            self.tables.append(Table(table_id=i, seats=table_seats, max_time_limit=self.max_time_limit))

    def reserve(self, guests_num, table_id) -> bool:
        for table in self.tables:
            if table.table_id == table_id:
                return table.reserve(guests_num)

        # table with provided id does not exist
        return False

    def release(self, table_id) -> bool:
        for table in self.tables:
            if table.table_id == table_id:
                return table.release()
        return False

    def get_available_tables(self, guests_num) -> list[Table]:
        """

        :param guests_num:
        :return: list of relevant tables sorted by seats ascending
        Note the return value must be list to preserve order!
        """

        available_tables = []

        for table in self.tables:
            if table.seats >= guests_num and table.is_available():
                available_tables.append(table)

        # sort by seats num ascending
        sorted_tables = []
        available_tables_len = len(available_tables)

        for i in range(available_tables_len):
            min_table = available_tables[0]
            min_table_idx = 0
            for table_idx, table in enumerate(available_tables):

                # comparing tuples
                if table.seats < min_table.seats:
                    min_table = table
                    min_table_idx = table_idx

            sorted_tables.append(min_table)
            available_tables.pop(min_table_idx)

        return sorted_tables

    def get_soonest_available_tables(self, guests_num) -> list[Table]:

        # get suitable tables
        suitable_tables: list[Table] = []

        for table in self.tables:
            if table.seats >= guests_num:
                suitable_tables.append(table)

        # sort
        sorted_tables = []
        suitable_tables_len = len(suitable_tables)

        for i in range(suitable_tables_len):
            min_table = suitable_tables[0]
            min_table_idx = 0

            for table_idx, table in enumerate(suitable_tables):

                # comparing tuples
                if (table.get_available_time(), table.seats) < (min_table.get_available_time(), min_table.seats):
                    min_table = table
                    min_table_idx = table_idx

            sorted_tables.append(min_table)
            suitable_tables.pop(min_table_idx)

        return sorted_tables


if __name__ == '__main__':

    restaurant = None

    try:
        if not os.path.exists("data.pickle"):
            # create a system for japanika
            restaurant = TableReservationSystem([3, 5, 2, 2, 6, 4, 3, 6], 'Japanika')
        else:
            with open("data.pickle", "rb") as f:
                restaurant:TableReservationSystem = pickle.load(f)
    except Exception:
        print("Cannot initialize our restaurant, do you want to create it from scratch?")

    try:
        # working with our restaurant
        # in your projects - a lot of code for user menu
        print(restaurant.tables[1])
        restaurant.reserve(4, 1)
        restaurant.reserve(2, 2)
        restaurant.reserve(1, 7)
        print(restaurant.tables[1])
    except TableException:
        print("error occurred")
        try:
            num = int(input())
        except:
            pass
    except ValueError:
        print("value error")
    except Exception:
        print("unknown error")
    finally:
        with open("data.pickle", "wb") as f:
            pickle.dump(restaurant, f)


