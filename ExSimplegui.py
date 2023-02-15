import PySimpleGUI as sg


class TelaPython:
    def __init__(self):

        # Criar layout
        layout = [
            [sg.Text('nome', size=(5, 0)), sg.Input(size=(20, 0), key='nome')],
            [sg.Text('idade', size=(5, 0)), sg.Input(size=(5, 0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('gmail', key='gmail'), sg.Checkbox('outlook', key='outlook'), sg.Checkbox('yahoo', key='yahoo')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('sim', 'cartes', key='aceitaCartao'), sg.Radio('Nao', 'cartoes', key='NaoAceitaCartao')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30, 15))]
        ]
        # criando a tela de exibição
        self.janela = sg.Window('Dados do usuário').layout(layout)

    def Iniciar(self):
        while True:

            # Extraindo dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['gmail']
            outlook = self.values['outlook']
            yahoo = self.values['yahoo']
            aceitaCartao = self.values['aceitaCartao']
            Naoaceitacartao = self.values['NaoAceitaCartao']
            print('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(nome, idade,
                  gmail, outlook, yahoo, aceitaCartao, Naoaceitacartao))


tela = TelaPython()
tela.Iniciar()


self.lista = print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(codmot, dtcte, numcte, v_frete, diesel, V_varla, v_pneu, v_oficina, v_desp_viag, v_outras_desp))
