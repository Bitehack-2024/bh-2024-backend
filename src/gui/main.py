import PySimpleGUI as sg
import os
from pathlib import Path
from zipfile import ZipFile

DATA_PATH = Path(__file__).parent.parent / "data"

# All the stuff inside your window.
layout = [  [sg.Text('Milo cie widziec drogi uzytkowniku')],
            [sg.Text('Jesli natrafiles na problem to jestes w dobrym miejscu. Wpisz co sie stalo, a twoj wnuczek zaraz sie tym zajmie.')],
            [sg.Text('Kiedy wystapil problem: '), sg.InputText()],
            [sg.Text('Krotki opis problemu: '), sg.InputText()],
            [sg.Button('Popros o pomoc'), sg.Button('Wyjdz')] ]

# Create the Window
window = sg.Window('Window Title', layout)

def list_files(directory_path):
    try:
        files = os.listdir(directory_path)
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        
        return files
    
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return []
    except PermissionError:
        print(f"Error: No permission to access directory '{directory_path}'.")
        return []

def submit_problem(date, description):
    print("Data:", date)
    print("Problem:", description)

    try:
        os.remove(DATA_PATH / 'files.zip')
    except:
        pass

    with ZipFile(DATA_PATH / 'files.zip', 'w') as myzip:
        for file in list_files(DATA_PATH):
            myzip.write(DATA_PATH / file)
    print("ZIP: created")

    return 1

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Wyjdz': break
    elif event == 'Popros o pomoc': submit_problem(values[0], values[1])
    

window.close()