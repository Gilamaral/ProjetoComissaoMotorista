import pandas as pd
import mysql.connector
import PySimpleGUI as sg



def ViagemM():
    

    senhahost = 'dulguiga16'
   
    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    mybd.cursor()
    
   
    df = pd.read_sql_query('select * from cte where codmot = 32;', mybd)
    tab2 = df.set_index('codmot')
    lista = tab2

    layout = [
            [sg.Multiline(size= (150, 200),default_text= df,)]
            #[ps.Output(size= (80, 30),s=(lista))]
             ]

    if mybd.is_connected():
        mybd.close()
        
    return sg.Window('cte', element_justification='center', layout=layout, size=(700, 300), finalize=True)

    

ViagemM()

while True:
    window, event, values = sg.read_all_windows()

'''
import PySimpleGUI as ps


def tela_ini():
    """
    -> Cria a janela inicial do programa.
    :return: Sem retorno.
    """
    lista = 'teste','teste'

    layout = [
            [ps.Multiline(size= (80, 30),default_text= lista,)]
            #[ps.Output(size= (80, 30),s=(lista))]
             ]


    return ps.Window('HealthCalc', icon='logo.ico', element_justification='center', layout=layout, size=(552, 300), finalize=True)

tela_ini()
while True:
    window, event, values = ps.read_all_windows()
'''
    