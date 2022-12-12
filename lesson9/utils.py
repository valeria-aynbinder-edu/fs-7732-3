def my_sum(l1: list[int], l2: list[int]) -> list[int]:
    ret_val = []
    for elem1, elem2 in zip(l1, l2):
        ret_val.append(elem1+elem2)
    return ret_val


# print("Hello")
