
import PySimpleGUI as sg
import mysql.connector


def TelaMenu():

    layout = [
        [sg.Button('Abrir Lanc', size=(20,0))],
        [sg.Button('Gerar Comissao', size=(20,0))]
    ]
    return sg.Window('menu', layout=layout, finalize=True, size=(800,500))

def Gravou():
    def TelaDados():

        layout = [
            [sg.Text('Codigo do motorista', size=(20, 0)),
                sg.Input(size=(5, 0), key='codmot')],
            [sg.Text('Data do Cte', size=(20, 0)),
                sg.Input(size=(10, 0), key='dtcte')],
            [sg.Text('Numero Cte', size=(20, 0)),
                sg.Input(size=(10, 0), key='numcte')],
            [sg.Text('Valor do frete', size=(20, 0)),
                sg.Input(size=(10, 0), key='v_frete')],
            [sg.Text('Diesel', size=(20, 0)), sg.Input(
                size=(10, 0), key='diesel')],
            [sg.Text('Arla', size=(20, 0)), sg.Input(
                size=(10, 0), key='V_varla')],
            [sg.Text('Pneu', size=(20, 0)), sg.Input(
                size=(10, 0), key='v_pneu')],
            [sg.Text('Desp. de oficina', size=(20, 0)),
                sg.Input(size=(10, 0), key='v_oficina')],
            [sg.Text('Valor desp viagem', size=(20, 0)),
                sg.Input(size=(10, 0), key='v_desp_viag')],
            [sg.Text('Outras despesas', size=(20, 0)),
                sg.Input(size=(10, 0), key='v_outras_desp')],
            [sg.Button('Enviar dados')],
            [sg.Button('voltar')]            
        ]

        return sg.Window('Lançamento CTE', layout=layout, finalize=True, size=(300, 350))

    tela_dados = None

    window, event, values = sg.read_all_windows()
 
    while True:

        tela_dados = TelaDados()

        window, event, values = sg.read_all_windows()

        if window == tela_dados and event == sg.WIN_CLOSED:
            window.close()
            break
        
        else:
            lista = None
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

            lista = [codmot, dtcte, numcte, v_frete, diesel, V_varla,v_pneu, v_oficina, v_desp_viag, v_outras_desp]
        
            mybd = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='dulguiga16',
                database='comissaom'
            )
            mycursor = mybd.cursor()
            if mybd.is_connected():
                print('conectado')

            gravar = "INSERT INTO cte (codmot, datacte, numcte, v_frete, diesel, V_varla, v_pneu, v_oficina, v_desp_viagem, v_outras_desp) VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)"
            lista = (codmot, dtcte, numcte, v_frete, diesel, V_varla,
                        v_pneu, v_oficina, v_desp_viag, v_outras_desp)

            mycursor.execute(gravar, lista)
            mybd.commit()
            print(mycursor.rowcount, "record inserted.")


menu = TelaMenu()
gravar = None

while True:

    window, event, values = sg.read_all_windows()

    if window == menu and event ==sg.WIN_CLOSED:
        break
    if window == menu and event == 'Abrir Lanc':
        gravar = Gravou()
        #menu.hide()
    #if window == gravar and event == sg.WIN_CLOSED:
        #menu()
   











'''
tela_menu, gravabd = TelaMenu(), None

while True:

    window, event, values = sg.read_all_windows()

    tela_menu()

    if window == tela_menu and event == sg.WIN_CLOSED:
        break

    if window == tela_menu and event == 'Abrir Lanc':
        gravabd = Gravou()
        tela_menu.hide()

'''