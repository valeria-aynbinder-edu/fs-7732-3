from lesson16.bank.customer import Customer


class BankAccount:

    def __init__(self, account_id, branch_id):
        self._account_id: int = account_id
        self._branch_id: int = branch_id
        self._balance: float = 0

    def set_branch_id(self, new_branch_id):
        self._branch_id = new_branch_id

    def withdraw(self, amnt: float) -> bool:
        new_balance = self._balance - amnt
        if new_balance >=0:
            self._balance = new_balance
            return True
        else:
            return False

    def deposit(self, amnt: float) -> bool:
        new_balance = self._balance + amnt
        self._balance = new_balance
        return True


    def get_balance(self):
        return self._balance

