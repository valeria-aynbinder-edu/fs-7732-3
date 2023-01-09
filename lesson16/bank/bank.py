from lesson16.bank.account import BankAccount
from lesson16.bank.address import Address
from lesson16.bank.branch import Branch
from lesson16.bank.customer import Customer


class Bank:

    def __init__(self, name, address: Address):
        self._name = name
        self._address = address
        self._branches: dict[int, Branch] = {}
        self._customers: dict[int, Customer] = {}
        self._accounts: dict[int, BankAccount] = {}
        self._account2customers: dict[int, set[Customer]] = {}
        self._customer2accounts: dict[int, set[BankAccount]] = {}

    def get_name(self):
        return self._name

    def get_address(self) -> Address:
        return self._address

    def add_branch(self, branch_id: int, name: str,
                   address: Address) -> bool:
        if branch_id in self._branches:
            return False
        branch = Branch(branch_id, name, address)
        self._branches[branch_id] = branch

    def get_branch_by_id(self, branch_id) -> Branch:
        return self._branches.get(branch_id)

    def get_branches_by_city(self, city) -> list[Branch]:
        ret_val = []
        for br_id, branch in self._branches.items():
            if branch.get_branch_address().get_city() == city:
                ret_val.append(branch)
        return ret_val

    def update_branch_address(self, branch_id, address: Address) -> bool:
        branch = self._branches.get(branch_id)
        if not branch:
            return False
        branch.set_branch_address(address)
        return True

    def remove_branch_by_id(self, branch_id) -> bool:
        if branch_id in self._branches:
            self._branches.pop(branch_id)
            return True
        else:
            return False

    def create_account(self, account_id, branch_id, customer_ids: set[int]) -> bool:
        """
        Creates a new account and associates it with provided customer ids.
        If customer with provided id does not exist - returns False
        :param account_id: the id of the new account
        :param branch_id: branch id of the new account
        :param customer_ids: ids of the customers that will become holders of this account
        :return:
        """
        account_holders = set()
        for customer_id in customer_ids:
            if customer_id not in self._customers:
                return False
            else:
                account_holders.add(self._customers[customer_id])
        account = BankAccount(account_id, branch_id)

        self._accounts[account_id] = account
        self._account2customers[account_id] = account_holders
        for customer_id in customer_ids:
            if customer_id not in self._customer2accounts:
                self._customer2accounts[customer_id] = set()
            self._customer2accounts[customer_id].add(account)

        return True

    def add_holder_to_account(self, account_id, customer_id) -> bool:
        if account_id not in self._accounts or customer_id not in self._customers:
            return False

        current_account_holders = self._account2customers[account_id]
        new_holder = self._customers[customer_id]
        account = self._accounts[account_id]
        if new_holder in current_account_holders:
            # this person already a holder for this account
            return False
        else:
            self._account2customers[account_id].add(new_holder)
            self._customer2accounts[customer_id].add(account)
            return True

    def withdraw(self, account_id, amnt) -> bool:
        if account_id not in self._accounts:
            return False
        account = self._accounts[account_id]
        return account.withdraw(amnt)

    def deposit(self, account_id, amnt) -> bool:
        if account_id not in self._accounts:
            return False
        account = self._accounts[account_id]
        return account.deposit(amnt)

    def transfer(self, account_id_from, account_id_to, amnt) -> bool:
        if account_id_from not in self._accounts or account_id_to not in self._accounts:
            return False

        account_from = self._accounts[account_id_from]
        account_to = self._accounts[account_id_to]

        if account_from.withdraw(amnt):
            account_to.deposit(amnt)
            return True




if __name__ == '__main__':
    bank = Bank("Discount",
                Address("Israel", "Tel Aviv", "Dizengoff", 12345, 6))
    # 1
    bank.add_branch(1, "kiryat hasharon",
                    Address("Israel", "Netanya", "Tom Lantos", 12345, 6))
    bank.add_branch(2, "aaaaa",
                    Address("Israel", "Tel Aviv", "Menahem Begin", 12345, 6))
    bank.add_branch(3, "bbbbb",
                    Address("Israel", "Tel Aviv", "Alenby", 12345, 6))

    branches = bank.get_branches_by_city("Netanya")
    for br in branches:
        if br.get_branch_name() == "kiryat hasharon":
            bank.update_branch_address(br.get_branch_id(), Address("Israel", "Netanya", "Tom Lantos", 12345, 9))
    # # 2
    # new_branch = Branch(5, "kiryat hasharon", Address("Israel", "Tel Aviv", "Dizengoff", 12345, 6))
    # bank.add_branch(new_branch)