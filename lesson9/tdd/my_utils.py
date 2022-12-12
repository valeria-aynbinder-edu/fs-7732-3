from typing import Any


def make_dict(orig_list: list[tuple[Any, Any]]) -> dict[Any, list]:
    ret_dict: dict[Any:list] = {}

    # iterate the original list
    for orig_key, orig_num in orig_list:

        # create an new key with empty list if key does not exist
        if orig_key not in ret_dict:
            ret_dict[orig_key] = [orig_num]

        # add new value to the list
        ret_dict[orig_key].append(orig_num)
    return ret_dict

