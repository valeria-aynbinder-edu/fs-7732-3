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
    print(re.search("ca*t", "cat"))
    print(re.search("ca*t", "caaaaaat"))

    print(re.search("ca*t", "ct"))
    print(re.search("(ca)*t", "ct"))
    print(re.search("[ca]*t", "ct"))
    print(re.search("[ca]*t", "cccacacaaaat"))
    print(re.search("[ca]*t", "64734834rsdgt"))
    print(re.search("c*a*t", "ccccccccccaaaaat"))

    print(re.search("ca?t", "ct"))
    print(re.search("ca?t", "cat"))
    print(re.search("ca?t", "caat"))

    print(re.search("ca{3,7}t", "caaat"))
    print(re.search("ca{3,7}t", "caaaaaaat"))
    print(re.search("ca{,7}t", "caaaaaaat"))
    print(re.search("ca{3,}t", "caaaaaaat"))
    print(re.search("ca{3}t", "caaaaaaat"))
    print(re.search("ca{3}t", "caaat"))

    # chen
    print(re.search("(dog|cat)( dog| cat)*", 'dog'))

    #lior
    # print(re.search("(cat |dog )(dog ?|cat ?)*", " dog cat dog cat "))

    print(re.search("[0-9].*[0-9]", "9sdfh%^-#ljde4"))
    print(re.search("[0-9]*[0-9]", "9sdfh%^-#ljde4"))

    print(re.search(".*[0-9]$", "dgffdhfhf8"))
    print(re.search(".*[0-9]$", "dgffdhfhf8a"))

    print(re.search("^[0-9].*", "7sdkfgjdh"))
    print(re.search("^[0-9].*", "a7sdkfgjdh"))

    print(re.search("[^0-9]", "%"))









    # print(re.search("0*[a-c]9+", "cat"))
    # print(re.search("0*[a-c]9+", "c"))
    # print(re.search("0*[a-c]9+", "0000c99999"))
    # print(re.search("0*[a-c]9+", "werwer0000c99999werwer"))


