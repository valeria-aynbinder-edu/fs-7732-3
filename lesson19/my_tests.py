import unittest

from lesson19.table_system import Table
from lesson19.table_exceptions import *


class TableTestCase(unittest.TestCase):
    def test_valid_reserve_table(self):
        table = Table(1, 3)
        table.reserve(2)
        self.assertFalse(table.is_available())
        self.assertEqual(table.occupied_seats, 2)

    def test_reserve_already_occupied(self):
        table = Table(1, 2)
        table.reserve(1)
        self.assertRaises(
            TableAlreadyReserved, Table.reserve,
            table, 1
        )


if __name__ == '__main__':
    unittest.main()
