# Option 1

seat = input("Seat: ")
structure = input("Structure: ")

char = seat[-1]
if len(seat) == 2:
    # 4J 6A
    row_num = seat[0]
else:
    # 45B 12C
    row_num = seat[:2]
#option 2
# row_num = seat[:-1]


batches = structure.split(" ")
# ABC DEFG HIJ
# ABC DEF
window_chars = [structure[0], structure[-1]]
aisle_chars = [batches[0][-1]]
aisle_chars.append(batches[1][0])

if len(batches) == 3:
    aisle_chars.append(batches[1][-1])
    aisle_chars.append(batches[2][0])

print(f"Window chars: {window_chars}")
print(f"Aisle chars: {aisle_chars}")

print(f"Row number: {row_num}")
print(f"Char: {char}")

if char in window_chars:
    print("Window")
elif char in aisle_chars:
    print("Aisle")
else:
    print("Middle")