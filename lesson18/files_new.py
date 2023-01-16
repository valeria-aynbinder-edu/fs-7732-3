from io import TextIOWrapper

relative_path = "data/alice_in_wonderland.txt"
#absolute_path = "/Users/valeria/src/lesson18/data/alice_in_wonderland.txt"

# file_descriptor = open(relative_path, 'r')
# # print(type(file_descriptor))
# # file_descriptor.read()
# content = file_descriptor.read(1000)
# content = file_descriptor.read(500)
# file_descriptor.seek(0)
# content = file_descriptor.read(500)
# print(len(content))
# print(content)
# file_descriptor.close()
#
#
# fd = open(relative_path, 'r')


# with open(relative_path, 'r') as fd:
#     content: str = fd.read(1000)
#     fd.read(500)
#     print(type(fd))
#     # print(content)
#
# print("after with block")
# # fd.read()
# print(fd.closed)
# print(content[100:200])

# with open(relative_path, 'r') as fd:
#     for i in range(10):
#         line = fd.readline()
#         print(line)

# with open(relative_path, 'r') as fd:
#     cnt = 0
#     for line in fd:
#         cnt += line.lower().count('alice')
#
# print(cnt)

def get_min_aapl_price():
    aapl_path = "data/AAPL.csv"

    min_price = None
    with open(aapl_path, 'r') as fd:
        # skip first line
        fd.readline()

        for line in fd:
            low_price = float(line.split(",")[1])
            if min_price is None or low_price < min_price:
                min_price = low_price
    return min_price

print(get_min_aapl_price())


def get_min_aapl_price():
    aapl_path = "data/AAPL.csv"

    min_price = None
    is_first_line = True
    with open(aapl_path, 'r') as fd:
        for line in fd:
            if is_first_line:
                is_first_line = False
                continue
            low_price = float(line.split(",")[1])
            if min_price is None or low_price < min_price:
                min_price = low_price
    return min_price



def get_min_aapl_price():
    aapl_path = "data/AAPL.csv"

    min_price = None
    with open(aapl_path, 'r') as fd:
        for i, line in enumerate(fd):
            if i == 0:
                continue
            low_price = float(line.split(",")[1])
            if min_price is None or low_price < min_price:
                min_price = low_price
    return min_price
