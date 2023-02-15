import PySimpleGUI as sg

def Menu():
    layout = [
        [sg.Button('Abrir Lanc')]
        [sg.button('Gerar Comissao')]
    ]

    return sg.Window('menu', layout=layout, finalize=True, size=(800,500))

menu1 = Menu()

