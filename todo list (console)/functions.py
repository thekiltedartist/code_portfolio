def get_todos(filepath='todo.txt'):
    """ Read text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todo.txt', ):
    """ Write the to-do items list in the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


def add_todos(user_arg):
    """ Takes the user argument `add and adds a new item"""
    todo = user_arg[4:]
    todos = get_todos()
    todos.append(todo + '\n')
    write_todos(todos)


def view_todos():
    """ Takes the argment `view and prints the list in the console """
    todos = get_todos()

    for index, item in enumerate(todos):
        item = item.strip('\n')
        item = item.title()
        row = f'{index + 1}-{item}'
        print(row)


def edit_todos(user_arg):
    """Takes the `edit command and lets you alter selected item"""
    try:
        number = int(user_arg[5:])
        number = number - 1

        todos = get_todos()

        new_task = input("Enter new Task: ")
        todos[number] = new_task + '\n'
    except ValueError:
        print("Command Not Valid")

    write_todos(todos)


def complete_todo(user_arg):
    """ Takes the 'complete command, prints the called item in the console and removes it from the list"""
    try:
        number = int(user_arg[9:])
        todos = get_todos()

        index = number - 1
        remove = todos[index].strip('\n')
        todos.pop(number - 1)
        write_todos(todos)

        print(f'Task {remove} has been completed!')
    except IndexError:
        print("Invalid Command")


def todo_loop(prompt_local):
    """A While loop that executes the commands of the to do list"""
    while True:
        user_action = input(prompt_local)
        user_action = user_action.strip()

        if user_action.startswith('add'):
            add_todos(user_action)
        elif user_action.startswith('view'):
            view_todos()
        elif user_action.startswith('edit'):
            edit_todos(user_action)
        elif user_action.startswith('complete'):
            complete_todo(user_action)
        elif user_action.startswith('exit'):
            break
        else:
            print("Command not Valid")
