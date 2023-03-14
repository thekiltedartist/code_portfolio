from functions import *
from time import strftime

# add text instrutions to users and declare list variable
prompt = "Add or View a Task, Edit, or Exit: "
todos = []
todo_file = 'todo.txt'
print("Welcome to the ToDo list.")
print(f'Today is {strftime("%b %d, %Y %H:%M:%S")}')

# user input for task list and show users what they added
todo_loop(prompt)

print("get tasks done!")
