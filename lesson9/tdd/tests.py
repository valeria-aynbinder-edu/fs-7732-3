from lesson9.tdd.my_utils import make_dict
import pprint


def test1():
    ret_val = make_dict([
        ('apples', 3.2),
        ('bananas', 5),
        ('mango', 4),
        ('apples', 2.5),
        ('apples', 6),
        ('bananas', 9.8)
    ])
    expected_output = {
        'apples': [3.2, 2.5, 6],
        'bananas': [5, 9.8],
        'mango': [4]
    }

    assert len(ret_val) == 3, f"Wrong list length: {len(ret_val)}"
    assert ret_val == expected_output, f"Wrong dictionary content:\n" \
            f"Expected:  {expected_output},\n" \
            f"received: {ret_val}"


def test2():
    ret_val = make_dict([])
    assert ret_val == {}, "Non-empty dict for empty input"


if __name__ == '__main__':
    test1()
    test2()
