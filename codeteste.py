import PySimpleGUI as sg

layout = [
    [sg.Text('Codigo do motorista', size=(20, 0)), sg.Input(size=(5, 0), key='codmot')],
    [sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Cal US No Buttons Location (0,0)', close_when_date_chosen=True,  target='-IN-', location=(0,0), no_titlebar=False, )],
    [sg.Text('Numero Cte', size=(20, 0)), sg.Input(size=(10, 0), key='numcte')],
    [sg.Text('Placa', size=(20, 0)), sg.Input(size=(10, 0), key='placa')],
    [sg.Text('Valor do frete', size=(20, 0)), sg.Input(size=(10, 0), key='v_frete')],
    [sg.Text('Diesel', size=(20, 0)), sg.Input(size=(10, 0), key='diesel')],
    [sg.Text('Arla', size=(20, 0)), sg.Input(size=(10, 0), key='V_varla')],
    [sg.Text('Pneu', size=(20, 0)), sg.Input(size=(10, 0), key='v_pneu')],
    [sg.Text('Desp. de oficina', size=(20, 0)), sg.Input(size=(10, 0), key='v_oficina')],
    [sg.Text('Valor desp viagem', size=(20, 0)), sg.Input(size=(10, 0), key='v_desp_viag')],
    [sg.Text('Outras despesas', size=(20, 0)), sg.Input(size=(10, 0), key='v_outras_desp')],
    [sg.Button('Enviar dados')]
]

sg.Window('Lançamento CTE', layout=layout, finalize=True, size=(300, 350))