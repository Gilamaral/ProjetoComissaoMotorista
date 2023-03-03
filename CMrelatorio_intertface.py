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

    print(df)
    
    tabpd1 = df
    grav1 = []

    for i in tabpd1.index:
        grav = [tabpd1['codmot'][i], tabpd1['datacte'][i], tabpd1['numcte'][i], tabpd1['v_frete'][i], tabpd1['V_varla'][i], tabpd1['diesel'][i], tabpd1['v_pneu'][i], tabpd1['v_oficina'][i], tabpd1['V_desp_viagem'][i], tabpd1['v_outras_desp'][i]]
        grav1.append(grav)

    titulo = ['Cod', 'Data', 'Cte', 'Frete', 'Arla', 'Diesel', 'Pneu', 'Oficina', 'D. Viagem', 'Out Desp']

    tbl1 = sg.Table(values=grav1,
                    headings=titulo,
                    auto_size_columns=False,
                    col_widths=50,
                    display_row_numbers=False,
                    text_color='black',
                    justification='center',
                    key='-TABLE-',
                    selected_row_colors='red on yellow',
                    enable_events=True,
                    expand_x=False,
                    expand_y=False,
                    alternating_row_color= 'grey',
                    background_color='white' ,
                    header_font=9,
                    enable_click_events=True)

    layout = [[tbl1]]

    window = sg.Window("Comissão por motorista", layout, size=(935, 200), resizable=True)

    while True:
        event, values = window.read()
        #print("event:", event, "values:", values)

        if event == sg.WIN_CLOSED:
            break



def ComissaoMtela():

    import pandas as pd
    import PySimpleGUI as sg
    import CMtelas_interface as cv
    import CMbd_interface as co
    
    #codmot = str(cv.Cst_mot())
    select = ('select * from comissao;')
    co.Consult_dados(select)
    df = co.Consult_dados(select)
    #df = df.loc[(df['codmot'] == codmot)]
    df = pd.DataFrame(df)

    tabpd1 = df
    grav1 = []

    for i in tabpd1.index:
        grav = [tabpd1['codmot'][i], tabpd1['faturado'][i], tabpd1['combustivel'][i], tabpd1['desp_viag'][i], tabpd1['out_desp'][i], tabpd1['comissao'][i]]
        grav1.append(grav)


    titulo = ['codmot', 'faturado', 'combustivel', 'desp_viag', 'out_desp', 'comissao']

    tbl1 = sg.Table(values=grav1,
                    headings=titulo,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    text_color='black',
                    justification='center',
                    key='-TABLE-',
                    selected_row_colors='red on yellow',
                    enable_events=True,
                    expand_x=False,
                    expand_y=False,
                    alternating_row_color= 'grey',
                    background_color='white' ,
                    header_font=12,
                    enable_click_events=True)

    layout = [[tbl1]]

    window = sg.Window("Comissão por motorista", layout, size=(600, 200), resizable=True)

    while True:
        event, values = window.read()
        #print("event:", event, "values:", values)

        if event == sg.WIN_CLOSED:
            break



def Multil():

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