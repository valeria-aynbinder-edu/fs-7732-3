from lesson16.bank.address import Address


class Branch:
    def __init__(self, branch_id: int, name: str, address: Address):
        self._branch_id: int = branch_id
        self._name: str = name
        self._address: Address = address

    def get_branch_id(self):
        return self._branch_id

    def get_branch_name(self):
        return self._name

    def get_branch_address(self) -> Address:
        return self._address

    def set_branch_address(self, new_address):
        self._address = new_address

    def __str__(self):
        return f"<Branch id: {self._branch_id}, name: {self._name}>"

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    address = Address("Israel", "Tel Aviv", "Dizengoff", 12345, 6)
    branch = Branch(300, "Dizengoff", address)
    print(branch)