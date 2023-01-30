import re


if __name__ == '__main__':

    result = re.search("a", "cat")
    print(type(result))
    print(result)
    print(re.search("b", "cat"))

    print(re.search("[af%#k]", "catk"))
    print(re.findall("[af%#k]", "catk"))

    print(re.search("[a-d]", "cat"))
    print(re.search("[abcd]", "cat"))
    print(re.search("abcd", "cat"))

    print(re.search("[1-9][A-Fa-f]", "9C"))
    print(re.search("[1-9][A-Fa-f]", "7465asfsh9Clajdfgh"))
    print(re.search("[1-9][A-F][a-f]", "9Cf"))
    print(re.search("[1-9][A-Fa-f1-9&%$#]", "9C"))
    print(re.search("[1-9] [@#$%] [a-z]!!!!!!!", "4 # f!!!!!!!"))  # 4 # f
    print(re.search("[1-9] [@#$%] [a-z]!!!!!!!", "gfhgjhjh sd 454 # f!!!!!!!fhfjgk"))
    print(re.search("cats (vs|with|against) dogs", "cats and dogs")) # cats vs dogs # cats with dogs
    print(re.search("cats (vs|with|against) dogs", "cats vs dogs"))

    # + * ?
    print(re.search("[1-9]+", "rtey65748536trgfb"))
    print(re.search("[1-9]+", "rtey6trgfb"))
    print(re.search("[1-9]+", "rteytrgfb"))
    print(re.search("[1-9]+", "rt56ey65748536trgfb"))
    print(re.search("[cat]+", "ccctttaatcat"))
    print(re.search("(cat)+", "ccctttaatcat"))
    print(re.search("(cat)+", "ccccacatcattttt"))
    print(re.search("cat+", "catttttt"))
    print(re.search("ca+t+", "catttttt"))
    print(re.search("ca+t+", "caaaaaaatttttt"))
    print(re.search("\+", "++++"))
    print(re.search("\++", "++++"))

    # print(re.search("0*[a-c]9+", "cat"))
    # print(re.search("0*[a-c]9+", "c"))
    # print(re.search("0*[a-c]9+", "0000c99999"))
    # print(re.search("0*[a-c]9+", "werwer0000c99999werwer"))


