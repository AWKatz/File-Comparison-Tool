import os
import shutil
import json
import PySimpleGUI as sg # type: ignore

#sg.theme('DarkGrey 15')
sg.theme('PythonPlus')

def compare_and_copy_files():
    layout = [[sg.ButtonMenu('Menu',  ['Menu', ['Save Setup::-SETUP-', 'Load Setup::-LOAD-']])],
              
        [sg.Text("Compare 2 files (local or remote) and then copy and overwrite the older file!")],
        [sg.HorizontalSeparator()],

        [sg.Text("Enter the path to the first file:", p=5), sg.FileBrowse(key="-FILE1-")],
         
        [sg.Text("Enter the path to the second file:", p=5), sg.FileBrowse(key="-FILE2-")], 
    
        [sg.HorizontalSeparator()],
        [sg.Button("Compare and Copy", border_width=0, button_color='black on yellow')],
        [sg.Button('Exit', border_width=0, button_color='black on red')] 
    ]

    window = sg.Window("Aaron's File Comparison Tool", layout, size=(500, 500), resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Compare and Copy":
            file1_path = values["-FILE1-"]
            file2_path = values["-FILE2-"]

            try:
                time1 = os.path.getmtime(file1_path)
                time2 = os.path.getmtime(file2_path)

                if time1 > time2:
                    shutil.copy2(file1_path, file2_path)
                    sg.popup(f"{file1_path} is newer. Copied to {file2_path}")
                elif time2 > time1:
                    shutil.copy2(file2_path, file1_path)
                    sg.popup(f"{file2_path} is newer. Copied to {file1_path}")
                else:
                    sg.popup("File are in sync, both files have the same modification time.")
            except FileNotFoundError:
                sg.popup("Files not found. Check the paths and try again.")

    window.close()

# Call the function
compare_and_copy_files()