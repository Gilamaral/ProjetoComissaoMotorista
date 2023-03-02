def Dados():

    import PySimpleGUI as sg

    layout = [
        [sg.Text('Codigo do motorista', size=(20, 0)), sg.Input(size=(5, 0), key='codmot')],
        [sg.Text('Data do Cte', size=(20, 0)), sg.Input(size=(10, 0), key='dtcte')],
        [sg.Text('Numero Cte', size=(20, 0)), sg.Input(size=(10, 0), key='numcte')],
        [sg.Text('Valor do frete', size=(20, 0)), sg.Input(size=(10, 0), key='v_frete')],
        [sg.Text('Diesel', size=(20, 0)), sg.Input(size=(10, 0), key='diesel')],
        [sg.Text('Arla', size=(20, 0)), sg.Input(size=(10, 0), key='V_varla')],
        [sg.Text('Pneu', size=(20, 0)), sg.Input(size=(10, 0), key='v_pneu')],
        [sg.Text('Desp. de oficina', size=(20, 0)), sg.Input(size=(10, 0), key='v_oficina')],
        [sg.Text('Valor desp viagem', size=(20, 0)), sg.Input(size=(10, 0), key='v_desp_viag')],
        [sg.Text('Outras despesas', size=(20, 0)), sg.Input(size=(10, 0), key='v_outras_desp')],
        [sg.Button('Enviar dados')]
    ]

    return sg.Window('Lançamento CTE', layout=layout, finalize=True, size=(300, 350))



def Cst_mot():
    
    import PySimpleGUI as sg

    layout = [[sg.Text('Digite o codigo do motorista: '), sg.Input(size=(5,0), key='mot')],
              [sg.Button('OK')]
              ]
    sg.Window(title='Consulta Viagem', layout=layout, finalize=True)

    while True:

        window, event, values = sg.read_all_windows()

        if event == 'OK':
            window.close()
            break
    codmot = values['mot']
    return(codmot)

