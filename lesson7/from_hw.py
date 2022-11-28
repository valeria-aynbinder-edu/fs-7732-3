# Write a Python function to execute a string containing
# Python code. Hint: search for exec() function in Python

def exec_code(code: str) -> None:
    print("Executing your code...")
    exec(code)
    print("Finished execution")

my_code = input("Insert your code: ")
exec_code(my_code)