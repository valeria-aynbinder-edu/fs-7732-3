from lesson12.ex1 import get_date_in_3_days


def test_same_week():
    
    print("Testing the same week dates...")
    orig = "2022-12-19, Mon, 10:00"
    ret_val = get_date_in_3_days(orig)
    assert ret_val == "Thursday"
    print("Test passed")


def test_next_week():
    print("Testing the next week dates...")
    orig = "2022-12-23, Fri, 15:00"
    ret_val = get_date_in_3_days(orig)
    assert ret_val == "Monday"
    print("Test passed")



if __name__ == '__main__':
    test_same_week()
    test_next_week()