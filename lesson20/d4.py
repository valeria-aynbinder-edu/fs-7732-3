# d4 - ex 2
def filter_out_vowels(word: str) -> str:
    return "".join(filter(lambda c: c not in "aAeEiIoOuU", word))


if __name__ == '__main__':
    print(filter_out_vowels('The Sun is shining'))