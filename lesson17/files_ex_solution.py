import os
import pprint


def get_csv_meta(path):
    with open(path) as f:
        rows_cnt = 0
        cols_cnt = len(f.readline().split(";"))
        for row in f:
            if row.strip():
                rows_cnt += 1
    return {'rows': rows_cnt, 'cols': cols_cnt}


def filter_csv(path):
    ret_dict = {}
    for root, dirs, files in os.walk(path):
        for filename in files:
            _, ext = os.path.splitext(filename)
            if ext == ".csv":
                full_path = os.path.join(root, filename)
                ret_dict[full_path] = get_csv_meta(full_path)
    return ret_dict

if __name__ == '__main__':
    pprint.pprint(filter_csv(os.path.join("data", "files_ex")))