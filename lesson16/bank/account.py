from lesson16.bank.customer import Customer


class BankAccount:

    def __init__(self, account_id, branch_id, owners_ids: list[int]):
        self._account_id = account_id
        self._branch_id = branch_id
        self._owners = owners_ids

    def set_branch_id(self, new_branch_id):
        self._branch_id = new_branch_id
