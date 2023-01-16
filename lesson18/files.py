import csv
import os

if __name__ == "__main__":
    relative_path = "data/alice_in_wonderland.txt"
    absolute_path = "/Users/valeria/src/zeiss/meeting3/files/data/alice_in_wonderland.txt"

    # file_handler = open(relative_path)
    # print(type(file_handler))
    # content = file_handler.read()
    # print(content)
    # file_handler.close()

    # context manager
    # with open(relative_path) as file_handler:
    #     content = file_handler.read()

    # read text file
    # with open(relative_path) as file_handler:
    #     counter = 0
    #     for line in file_handler:
    #         counter += line.count("Alice")
    #         # print(line)
    #     print(counter)

    # write to file
    # with open("./data/my_file.txt", "w") as fh:
    #     fh.write("Hello world\nHi")

    # with open("./data/my_file.txt", "a") as fh:
    #     fh.write("Valeria")


    # reading csv - basic
    # with open("./data/AAPL.csv", "r") as fh:
    #     for line in fh:
    #         row_list = line.split(",")
    #         print(f"The Open price in date {row_list[0]} is: {row_list[2]}")


    # reading from csv using DictReader
    # with open("./data/AAPL.csv") as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         print(f"The Open price in date {row['Date']} is: {row['Open']}")

    # root: Prints out directories only from what you specified.
    # dirs: Prints out sub-directories from the root.
    # files: Prints out all files from root and directories.

    # iterate over files in
    # that directory
    # for root, dirs, files in os.walk(".."):
        # print(f"root: {root} | dirs: {dirs} | files: {files}")
        # for filename in files:
            # print(f"{root}/{filename}")
            # print(root, dirs, filename)
            # print(os.path.join(root, filename))


    # print(os.sep)
    # print(os.path.exists(relative_path))
    # print(os.path.exists("./filess.py"))
    # print(os.path.abspath("./data/alice_in_wonderland.txt"))
    # print(os.path.relpath("/Users/valeria/src/zeiss/meeting3/files/data/alice_in_wonderland.txt", "."))
    # print(os.path.split("/Users/valeria/src/zeiss/meeting3/files/data/alice_in_wonderland.txt"))



    # os.makedirs("./data/new_data/bla/bla")
    # header = "first_name, last_name\n"
    # line1 = "valeria, aynbinder\n"
    # line2 = "brad, pitt\n"
    # rows = [header, line1, line2]
    # with open("./data/new_data/bla/bla/test.csv", "w") as fh:
    #     fh.writelines(rows)