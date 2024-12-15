import PySimpleGUI as sg
import os
from pathlib import Path
from zipfile import ZipFile
from time import sleep

DATA_PATH = Path(__file__).parent.parent / "data"

layout = [  [sg.Text('Milo cie widziec drogi uzytkowniku')],
            [sg.Text('Jesli natrafiles na problem to jestes w dobrym miejscu. Wpisz co sie stalo, a twoj wnuczek zaraz sie tym zajmie.')],
            [sg.Text('Kiedy wystapil problem: '), sg.InputText()],
            [sg.Text('Krotki opis problemu: '), sg.InputText()],
            [sg.Button('Popros o pomoc'), sg.Button('Wyjdz')] ]

window = sg.Window('Click Dziadek', layout)

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
    except Exception as e:
        print(e)

    files = list_files(DATA_PATH)

    with ZipFile(DATA_PATH / 'files.zip', 'w') as myzip:
        for file in files:
            if file == ".gitkeep":
                continue
            myzip.write(DATA_PATH / file, arcname=file)
    print("ZIP: created")

    return 1

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Wyjdz': break
    elif event == 'Popros o pomoc': submit_problem(values[0], values[1])
    

window.close()