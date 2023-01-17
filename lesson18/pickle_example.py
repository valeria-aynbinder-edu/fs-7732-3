import pickle

class BankAccount:
    def __init__(self, account_num, owner_name):
        self.account_num = account_num
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amnt):
        self.balance += amnt


class Bank:

    def __init__(self, bank_name):
        self.name = bank_name
        self.accounts: list[BankAccount] = []

    def add_account(self, account_num, owner_name):
        self.accounts.append(BankAccount(account_num, owner_name))
#
# if __name__ == '__main__':
#     bank = Bank("Hapoalim")
#     bank.add_account(123, 'David')
#     bank.add_account(234, 'Moshe')
#     bank.accounts[0].deposit(100)
#     bank.accounts[1].deposit(200)
#
#     with open("data/bank.pickle", "wb") as f:
#         pickle.dump(bank, f)


if __name__ == '__main__':
    with open("data/bank.pickle", "rb") as f:
        ret_val:Bank = pickle.load(f)
    print(ret_val.accounts[0].owner_name)