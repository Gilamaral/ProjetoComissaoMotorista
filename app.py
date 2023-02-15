import PySimpleGUI as sg
import pandas as pd
import mysql.connector


class Bdenvio:
    def __init__(self):
        # Criar layout
        layout = [
            [sg.Text('codmot', size=(12, 0)), sg.Input(size=(5, 0), key='codmot')],
            [sg.Text('dtcte', size=(12, 0)), sg.Input(size=(10, 0), key='dtcte')],
            [sg.Text('numcte', size=(12, 0)), sg.Input(size=(10, 0), key='numcte')],
            [sg.Text('v_frete', size=(12, 0)), sg.Input(size=(10, 0), key='v_frete')],
            [sg.Text('diesel', size=(12, 0)), sg.Input(size=(10, 0), key='diesel')],
            [sg.Text('V_varla', size=(12, 0)), sg.Input(size=(10, 0), key='V_varla')],
            [sg.Text('v_pneu', size=(12, 0)), sg.Input(size=(10, 0), key='v_pneu')],
            [sg.Text('v_oficina', size=(12, 0)), sg.Input(size=(10, 0), key='v_oficina')],
            [sg.Text('v_desp_viag', size=(12, 0)), sg.Input(size=(10, 0), key='v_desp_viag')],
            [sg.Text('v_outras_desp', size=(12, 0)), sg.Input(size=(10, 0), key='v_outras_desp')],
            [sg.Button('Enviar dados')],
            ]
    
        # criando a tela de exibição
        self.janela = sg.Window('Lançamento CTE').layout(layout)

    def Iniciar(self):
        while True:
            # Extraindo dados da tela
            self.button, self.values = self.janela.Read()
            codmot = self.values['codmot']
            dtcte = self.values['dtcte']
            numcte = self.values['numcte']
            v_frete = self.values['v_frete']
            diesel = self.values['diesel']
            V_varla = self.values['V_varla']
            v_pneu = self.values['v_pneu']
            v_oficina = self.values['v_oficina']
            v_desp_viag = self.values['v_desp_viag']
            v_outras_desp = self.values['v_outras_desp']
            lista = [codmot, dtcte, numcte, v_frete, diesel, V_varla, v_pneu, v_oficina, v_desp_viag, v_outras_desp]
            
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
            lista = (codmot, dtcte, numcte, v_frete, diesel, V_varla, v_pneu, v_oficina, v_desp_viag, v_outras_desp)

            mycursor.execute(gravar, lista)
            mybd.commit()
            print(mycursor.rowcount, "record inserted.")
            


tela = Bdenvio()
tela.Iniciar()
