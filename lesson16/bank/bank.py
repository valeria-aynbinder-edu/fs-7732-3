from lesson16.bank.account import BankAccount
from lesson16.bank.address import Address
from lesson16.bank.branch import Branch
from lesson7.gadget_store import Customer


class Bank:

    def __init__(self, name, address: Address):
        self._name = name
        self._address = address
        self._branches: dict[int, Branch] = {}
        self._customers: dict[int, Customer] = {}
        self._accounts: dict[int, BankAccount] = {}




    def get_name(self):
        return self._name

    def get_address(self) -> Address:
        return self._address

    # CRUD
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

    def add_account(self, account_id, branch_id,
                    customer_ids: list[int]) -> bool:
        for i in customer_ids:
            if i not in self._customers:
                return False
        account = BankAccount(account_id, branch_id, customer_ids)
        self._accounts[account_id] = account




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