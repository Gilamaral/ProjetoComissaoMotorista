import PySimpleGUI as sg
import mysql.connector



def Dados():

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



def LancarCte():

    while True:

        tela_dados = Dados()

        window, event, values = sg.read_all_windows()


        if window == tela_dados and event == sg.WIN_CLOSED:
            window.close()
            break
        
        else:           

            codmot = values['codmot']
            dtcte = values['dtcte']
            numcte = values['numcte']
            v_frete = values['v_frete']
            diesel = values['diesel']
            V_varla = values['V_varla']
            v_pneu = values['v_pneu']
            v_oficina = values['v_oficina']
            v_desp_viag = values['v_desp_viag']
            v_outras_desp = values['v_outras_desp']

            lista = (codmot, dtcte, numcte, v_frete, diesel, V_varla, v_pneu, v_oficina, v_desp_viag, v_outras_desp)
            gravar = "INSERT INTO cte (codmot, datacte, numcte, v_frete, diesel, V_varla, v_pneu, v_oficina, v_desp_viagem, v_outras_desp) VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)"
            
            mybd = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='dulguiga16',
                database='comissaom'
            )
            mycursor = mybd.cursor()
            if mybd.is_connected():
                print('conectado')

            mycursor.execute(gravar, lista)
            mybd.commit()
            print(mycursor.rowcount, "record inserted.")
            mybd.close()
            window.close()
