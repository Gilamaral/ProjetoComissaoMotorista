def ViagemM():
    import pandas as pd
    import PySimpleGUI as sg
    import CMtelas_interface as cv
    import CMbd_interface as co
    
    codmot = int(cv.Cst_mot())
    select = ('select * from cte;')
    co.Consult_dados(select)
    df = co.Consult_dados(select)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)
    #print(df)


    sg.popup(df, title='Relatorio de viagens realizadas', font=('', 10,''), line_width=1200)


def ComissaoM():
    import pandas as pd
    import PySimpleGUI as sg
    import CMtelas_interface as cv
    import CMbd_interface as co
    
    codmot = str(cv.Cst_mot())
    select = ('select * from comissao;')
    co.Consult_dados(select)
    df = co.Consult_dados(select)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)
    #print(df)
    
    sg.popup(df, title='Relatório de Comissões', font=('', 10,''), line_width=1200)


def ViagemMtela():

    import pandas as pd
    import PySimpleGUI as sg
    import CMtelas_interface as cv
    import CMbd_interface as co
    
    codmot = int(cv.Cst_mot())
    select = ('select * from cte;')
    co.Consult_dados(select)
    df = co.Consult_dados(select)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)
    #print(df)

    tabela = [[sg.Multiline(size=(90, 15), default_text=df,)]]

    sg.Window(title='Consulta Viagem', layout=tabela, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            break


def ComissaoMtela():

    import pandas as pd
    import PySimpleGUI as sg
    import CMtelas_interface as cv
    import CMbd_interface as co
    
    codmot = str(cv.Cst_mot())
    select = ('select * from comissao;')
    co.Consult_dados(select)
    df = co.Consult_dados(select)
    df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)

    tabela = [[sg.Multiline(size=(70, 5), default_text=df,)]]

    sg.Window(title='Consulta Comissão', layout=tabela, finalize=True)
    
    while True:
        window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            break
