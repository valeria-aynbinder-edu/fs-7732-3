from lesson11.c3_simple_sol import BankAccount

if __name__ == '__main__':

    a = BankAccount("discount", "tel aviv", 12345,
                    {"id": 12345678,
                     "name": "val",
                     "address": "bla"})

    # a.set_holder_address("new address")
    # a.holders["address"] = "new"
    # a.holders["id"] = 123457677

    print(a.get_holder())