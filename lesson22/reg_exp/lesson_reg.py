import re



if __name__ == '__main__':
    print(re.search("a", "cat"))
    print(re.search("0*[a-c]9+", "cat"))
    print(re.search("0*[a-c]9+", "c"))
    print(re.search("0*[a-c]9+", "0000c99999"))
    print(re.search("0*[a-c]9+", "werwer0000c99999werwer"))