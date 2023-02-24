def Cst_ViagemM():
    
    import PySimpleGUI as sg

    layout = [[sg.Text('Digite o codigo do motorista: '), sg.Input(size=(5,0), key='mot')],
              [sg.Button('OK')]
              ]
    sg.Window(title='Consulta Viagem', layout=layout, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        codmot = values['mot']
        if event == 'OK':
            window.close()
            break

def ViagemM():
    import pandas as pd
    import mysql.connector
    import PySimpleGUI as sg
    
    layout = [[sg.Text('Digite o codigo do motorista: '), sg.Input(size=(5,0), key='mot')],
              [sg.Button('OK')]
              ]
    sg.Window(title='Consulta Viagem', layout=layout, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        codmot = values['mot']
        if event == 'OK':
            window.close()
            break

    senhahost = 'dulguiga16'
   
    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    codmot = int(codmot)
    mybd.cursor()
    df = pd.read_sql('select * from cte;', mybd)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)
    sg.popup(df, title='Relatorio de viagens realizadas', font=('', 10,''), line_width=1200)

    df = df.to_excel('Viagens.xlsx')

    if mybd.is_connected():
        mybd.close()    
        
    return


def ComissaoM():
    import pandas as pd
    import PySimpleGUI as sg
    import mysql.connector

    layout = [[sg.Text('Digite o codigo do motorista: '), sg.Input(size=(5,0), key='mot')],
              [sg.Button('OK')]
              ]
    sg.Window(title='Consulta Viagem', layout=layout, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        codmot = values['mot']
        if event == 'OK':
            window.close()
            break

    senhahost = 'dulguiga16'

    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    #codmot = int(codmot)
    mybd.cursor()
    df = pd.read_sql_query('select * from comissao;', mybd)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)
    sg.popup(df, title='Relatório de Comissões', font=('', 10,''), line_width=1200)
    
    #df.to_excel('Comissao.xlsx')

    if mybd.is_connected():
        mybd.close()
        #print('desconectado')
    return


def ViagemMtela():

    import pandas as pd
    import mysql.connector
    import PySimpleGUI as sg

    layout = [[sg.Text('Digite o codigo do motorista: '), sg.Input(size=(5,0), key='mot')],
            [sg.Button('OK')]
            ]
    sg.Window(title='Consulta Viagem', layout=layout, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        codmot = values['mot']
        if event == 'OK':
            window.close()
            break
       
    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='dulguiga16',
        database='comissaom'
    )
    mybd.cursor()
    codmot = int(codmot)
    df = pd.read_sql_query('select * from cte;', mybd)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)

    tabela = [[sg.Multiline(size=(90, 15), default_text=df,)]]

    sg.Window(title='Consulta Viagem', layout=tabela, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            break


    if mybd.is_connected():
        mybd.close()


def ComissaoMtela():

    import pandas as pd
    import mysql.connector
    import PySimpleGUI as sg

    layout = [[sg.Text('Digite o codigo do motorista: '), sg.Input(size=(5,0), key='mot')],
            [sg.Button('OK')]
            ]
    sg.Window(title='Consulta Viagem', layout=layout, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        codmot = values['mot']
        if event == 'OK':
            window.close()
            break
       
    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='dulguiga16',
        database='comissaom'
    )
    mybd.cursor()
    codmot = codmot
    df = pd.read_sql_query('select * from comissao;', mybd)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)

    tabela = [[sg.Multiline(size=(70, 5), default_text=df,)]]

    sg.Window(title='Consulta Comissão', layout=tabela, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            break


    if mybd.is_connected():
        mybd.close()

