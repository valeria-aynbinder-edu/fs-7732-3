import csv
import os
import pprint


def get_csv_data(dir_path):
    if not os.path.exists(dir_path):
        raise Exception("Directory does not exists")

    ret_val = {}

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            # prefix, extension = os.path.splitext(file_path)
            # if extension == ".csv"
            if file_path.endswith(".csv"):
                with open(file_path) as csvfile:
                    reader = csv.DictReader(csvfile)
                    rows_num = 0
                    for row in reader:
                        rows_num += 1
                        cols = len(row)
                ret_val[file_path] = {'cols': cols, 'rows': rows_num}
    return ret_val

if __name__ == '__main__':
    path = "/Users/valeria/src/fs-7732-3/lesson18/data/files_ex"
    pprint.pprint(get_csv_data(path))
    # print(os.path.sep)