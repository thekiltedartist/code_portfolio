import functions, time
import PySimpleGUI as gui

gui.theme("Black")

label = gui.Text("Add Something To Get Done")
clock = gui.Text('', key='clock')
input_box = gui.InputText(tooltip="Do Something", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = gui.Button('Edit')
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")


window = gui.Window("The Get Stuff Done",
                    layout=[[clock],[label], [input_box, add_button], [list_box,edit_button, complete_button],[exit_button]],
                    font=('Ariel', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            try:
                todos = functions.get_todos()
                new_todo = values['todo'] + '\n'
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Please enter a ToDo item!")

        case "Edit":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Please select and item")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                gui.popup("Please Select an Item.")
        case "Exit":
            break

        case gui.WIN_CLOSED:
            break

window.close()
