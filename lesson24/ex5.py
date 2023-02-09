import os.path


def validate_file_exists(file_path: str) -> callable:
    def wrapper(original_func: callable) -> callable:
        def wrapping_function(*args, **kwargs):
            if not os.path.exists(file_path):
                raise Exception(
                    f"File {file_path} does not exist")
            return original_func(*args, **kwargs)
        return wrapping_function
    return wrapper


@validate_file_exists('config.ini')
def connect_to_db():
    pass

# connect_to_db = validate_file_exists('config.ini')(connect_to_db)
# connect_to_db = wrapper(connect_to_db)



@validate_file_exists('config_test.ini')
def connect_to_block_storage():
    pass


def do_something():
    pass


if __name__ == '__main__':
    connect_to_db()
    connect_to_block_storage()