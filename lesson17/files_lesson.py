# read from file
import string

relative_path = "data/alice_in_wonderland.txt"
absolute_path = "/Users/valeria/src/morning-ninjas/lesson9/files/data/alice_in_wonderland.txt"

# file_handler = open(relative_path, 'r')
# print(file_handler)
# #do stuff
# file_handler.close()

# with open(relative_path, 'r') as file_handler:
#     words_count = 0
#     check_first_space = False
#     while True:
#         c = file_handler.read(1000)
#         if not c:
#             break
#         if check_first_space and c[0] in string.whitespace:
#             words_count += 1
#         if c[-1] in string.whitespace:
#             words_count += len(c.split())
#         else:
#             words_count += len(c.split()) - 1
#             check_first_space = True
# print(words_count)
    # content = file_handler.read()
    # print(content[100: 1000])
    # print(content[::-1])

# print(content[content.index("CHAPTER II"):content.index("CHAPTER III")])
# print(len(content.split()))
# print(content.split()[100:200])

# price_sum = 0
# price_cnt = 0
# with open('data/AAPL.csv', 'r') as fh:
#     # skip 1st line
#     fh.readline()
#     for line in fh:
#         open_price = float(line.split(',')[2])
#         price_cnt += 1
#         price_sum += open_price
#
# print(price_sum/price_cnt)

# import csv
#
# csv.DictReader