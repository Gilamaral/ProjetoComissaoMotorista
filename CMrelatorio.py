
def ViagemM():
    import pandas as pd
    import mysql.connector
    import PySimpleGUI as sg
    import os

    senhahost = 'dulguiga16'
   
    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    mybd.cursor()
    
    #cst_codmot = int(input('Digite o motorista: ')])
    
    #tabpd = ('select * from cte;')
    df = pd.read_sql('select * from cte;', mybd)
    tab2 = df.set_index('codmot')
    #df = df.loc[df['codmot'] == cst_codmot]
    sg.popup(tab2, title='teste', font=('', 10,''), line_width=1200)

    #sair = input('Digite Enter para fechar')
    #print('Fim do relatorio!')

    if mybd.is_connected():
        mybd.close()
        #print('desconectado')
    return


def ComissaoM():
    import pandas as pd
    import PySimpleGUI as sg
    import mysql.connector

    senhahost = 'dulguiga16'

    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    mybd.cursor()
   
    #tabpd = ('select * from comissao;')
    df = pd.read_sql('select * from comissao;', mybd)
    tab2 = df.set_index('codmot')
    #df.to_excel('Comissao.xlsx')
    sg.popu(tab2, title='teste')

    sair = input('Digite Enter para fechar')
    print('Fim do relatorio!')

    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return


ViagemM()
