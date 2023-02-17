import PySimpleGUI as sg


def janela_login():
    layout=[
        [sg.Text('nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():
    layout=[
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Peperonni', key='pizza1'), sg.Checkbox('Pizza de frango com catupiri', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido1')]      
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)



janela1, janela2 = janela_login(), None

while True:

    window, event, values = sg.read_all_windows()

    if window == janela1 and event ==sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    
    if window == janela2 and event == 'Fazer Pedido1':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza Peperonni e Pizza de frango com catupiri')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza Peperonni')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza de frango com catupiri')
