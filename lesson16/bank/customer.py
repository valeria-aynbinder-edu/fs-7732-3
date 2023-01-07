from address import Address


class Customer:
    def __init__(self, customer_id: int, passport_id: int, name: str, surname: str,
                 phone_number: str, address: Address, salary: int, account_ids: list[int]) -> None:
        self.__customer_id: int = customer_id
        self.__passport_id: int = passport_id
        self.__name: str = name
        self.__surname: str = surname
        self.__phone_number: str = phone_number
        self.__address: Address = address
        self.__salary: int = salary
        self._accounts = account_ids

    def get_customer_id(self) -> int:
        return self.__customer_id

    def get_customer_passport_id(self) -> int:
        return self.__passport_id

    def get_customer_name(self) -> str:
        return self.__name

    def set_customer_name(self, name: str) -> None:
        self.__name = name

    def get_customer_surname(self) -> str:
        return self.__surname

    def set_customer_surname(self, surname: str) -> None:
        self.__surname = surname

    def get_customer_phone_number(self) -> str:
        return self.__phone_number

    def set_customer_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def get_customer_address(self) -> Address:
        return self.__address

    def set_customer_address(self, address: Address) -> None:
        self.__address = address

    def get_customer_salary(self) -> int:
        return self.__salary

    def set_customer_salary(self, salary: int) -> None:
        self.__salary = salary

    def add_bank_account(self) -> None:
        pass

    def remove_bank_account(self) -> None:
        pass