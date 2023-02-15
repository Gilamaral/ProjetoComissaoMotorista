import PySimpleGUI as sg
import app

def Menu():
    layout = [
        [sg.Button('abrir Lanc')]
    ]

    return sg.Window('menu', layout=layout, finalize=True, size=(800,500))

menu1 = Menu()


while True:
    menu1()

    window, event, values = sg.read_all_windows()

    if window == menu1 and event ==sg.WIN_CLOSED:
        break
    if window == menu1 and event == 'abrir Lanc':
        app.LancDados()
        