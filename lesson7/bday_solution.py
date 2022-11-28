COMMANDS = ("insert", "lookup", "quit")
bday_dict = {}


def get_command() -> str:
    while True:
        command = input("Insert command (insert, lookup, quit): ")
        if command not in COMMANDS:
            print("Invalid command, try again")
        else:
            return command


def insert_bday():
    name = input("Insert name: ")
    bday = input(f"Insert bday for {name}: ")
    bday_dict[name] = bday


def lookup_bday():
    name = input("Insert name: ")
    if name in bday_dict:
        print(f"{name}'s birthday is {bday_dict[name]}")
    else:
        print(f"Birth date for {name} does not exist")


while True:
    cmd = get_command()
    if cmd == "insert":
        insert_bday()
    elif cmd == "lookup":
        lookup_bday()
    else:
        print("Bye-bye")
        exit(0)