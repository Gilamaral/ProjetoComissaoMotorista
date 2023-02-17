import PySimpleGUI as sg

def Menu():

    layout = [
        [sg.Button('Abrir Lanc', size=(20,0))],
        [sg.Button('Gerar Comissao', size=(20,0))]
    ]
    return sg.Window('menu', layout=layout, finalize=True, size=(800,500))


menu1 = Menu()


while True:

     window, event, values = sg.read_all_windows()

     if window == menu1 and event ==sg.WIN_CLOSED:
        break
      
     #if window == menu1 and event =='Abrir Lanc':
       # lanc.Dados()
