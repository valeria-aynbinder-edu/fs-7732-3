# Implement a code that receives the layout of the seats in the aircraft as
# letters and returns the layout as numbers. For example:
# For example, for input: ABC DEF, you should print out: 3 3
# AB CDEF GH => 2 4 2
# You can assume that the maximum number of seat “batches” in any aircraft is 3.
#

seats = input("Enter the letters of the seats in the plane:")
count = seats.count(" ")
seats = seats.split(" ")
if count == 2:
    print(len(seats[0]), len(seats[1]), len(seats[2]))
elif count == 1:
    print(len(seats[0]), len(seats[1]))
else:
    print(len(seats[0]))