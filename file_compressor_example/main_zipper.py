import PySimpleGUI as gui
from zip_functions import make_archive

label1 = gui.Text("Select file to compress")
input1 = gui.Input()
button1 = gui.FileBrowse("Choose", key='files')

lable2 = gui.Text("Select Destination Folder")
input2 = gui.Input("Choose", key='folder')
button2 = gui.FolderBrowse()
button3 = gui.Button("Zip It! Zip It Good!")
output = gui.Text(key="output", text_color="green")
window = gui.Window("Rusty Zipper", layout=[[label1, input1, button1], [lable2, input2, button2], [button3, output]])
while True:
    event, values = window.read()
    filepaths = values['files'].split(',')
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="File Zipped")

window.close()