FILEPATH = "todos_item.txt"

def get_todos(filepath=FILEPATH):
    """ Read a Text file amd return
    the list of to-do item
    """
    with open(filepath, 'r') as file_local:
        todoos = file_local.readlines()
    return todoos

def write_todos(todos_arg, filepath=FILEPATH):
    """ write the to_do item in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())