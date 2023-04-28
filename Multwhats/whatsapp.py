def WhatsImg(msg1, msg2, msg3):

    import time

    import ML_Bd_sqlite as bd
    from PIL import Image as i
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    # Crie uma instância do driver do Chrome
    driver = webdriver.Chrome()

    # Abra o WhatsApp Web e faça o login na sua conta do WhatsApp
    driver.get("https://web.whatsapp.com")

    while len(driver.find_elements(By.ID, "side")) < 1:
        time.sleep(1)

    select = (f'select celfone, enviado, count(ID) from whatsapp where grupo = 1 group by celfone order by enviado desc;')
    bd.Consult_dados(select)
    df = bd.Consult_dados(select)

    # msg1 = 'TMS Completo, Modular e Customizável'
    # msg2 = 'Saiba mais pelo WhatsApp 5544999029337'
    # msg3 = 'Visite nosso site: https://www.apptruckar.com.br/'

    for fone in df.index:
        numcont = df['celfone'][fone]
        msg = f'{msg1}\n {msg2} \n {msg3}'

        # Encontre o campo de pesquisa e digite o nome ou número do contato
        contato = None
        while not contato:
            try:
                contato = driver.find_element(
                    By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
                contato.send_keys(numcont)
                time.sleep(1)
                contato.send_keys(Keys.ENTER)
            except:
                continue

        time.sleep(2)

        # Localize o campo de texto e digite a mensagem
        campo_mensagem = None
        while not campo_mensagem:
            try:
                campo_mensagem = driver.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                campo_mensagem.send_keys(Keys.CONTROL + 'v')
                time.sleep(2)
                driver.find_element(
                    By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
                time.sleep(3)
                campo_mensagem = driver.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                campo_mensagem.send_keys(msg)
                time.sleep(2)
                enter = driver.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                enter.send_keys(Keys.ENTER)
                time.sleep(2)
            except:
                continue

        time.sleep(3)

        update = (f'update whatsapp set enviado = 1 where celfone ={numcont};')
        bd.Update_dados(update)

    # Encerre o navegador
    driver.quit()


def Whats(msg1, msg2, msg3):

    import time

    import ML_Bd_sqlite as bd
    from PIL import Image as i
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    # Crie uma instância do driver do Chrome
    driver = webdriver.Chrome()

    # Abra o WhatsApp Web e faça o login na sua conta do WhatsApp
    driver.get("https://web.whatsapp.com")

    while len(driver.find_elements(By.ID, "side")) < 1:
        time.sleep(1)

    select = (f'select celfone, enviado, count(ID) from whatsapp where grupo = 1 group by celfone order by enviado desc;')
    bd.Consult_dados(select)
    df = bd.Consult_dados(select)

    # msg1 = 'TMS Completo, Modular e Customizável'
    # msg2 = 'Saiba mais pelo WhatsApp 5544999029337'
    # msg3 = 'Visite nosso site: https://www.apptruckar.com.br/'

    for fone in df.index:
        numcont = df['celfone'][fone]
        msg = f'{msg1}\n {msg2} \n {msg3}'

        # Encontre o campo de pesquisa e digite o nome ou número do contato
        contato = None
        while not contato:
            try:
                contato = driver.find_element(
                    By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
                contato.send_keys(numcont)
                time.sleep(1)
                contato.send_keys(Keys.ENTER)
            except:
                continue

        time.sleep(2)

        # Localize o campo de texto e digite a mensagem
        campo_mensagem = None
        while not campo_mensagem:
            try:
                campo_mensagem = driver.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                campo_mensagem.send_keys(msg)
                time.sleep(2)
                enter = driver.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                enter.send_keys(Keys.ENTER)
                time.sleep(2)
            except:
                continue

        time.sleep(3)

        update = (f'update whatsapp set enviado = 1 where celfone ={numcont};')
        bd.Update_dados(update)

    # Encerre o navegador
    driver.quit()


def AppWhats():

    import ML_Bd_sqlite as bd
    import PySimpleGUI as sg

    select = (f'select celfone, enviado, grupo from whatsapp;')
    bd.Consult_dados(select)
    df = bd.Consult_dados(select)

    tabpd1 = df
    grav1 = []

    for i in tabpd1.index:
        grav = [tabpd1['celfone'][i], tabpd1['enviado'][i], tabpd1['grupo'][i]]
        grav1.append(grav)

    titulo = ['Numero celular', 'Enviado', 'Grupo']

    tbl1 = sg.Table(values=grav1,
                    headings=titulo,
                    auto_size_columns=True,
                    col_widths=50,
                    display_row_numbers=True,
                    num_rows=3,
                    text_color='black',
                    justification='center',
                    key='-TABLE-',
                    selected_row_colors='red on yellow',
                    enable_events=True,
                    expand_x=False,
                    expand_y=False,
                    alternating_row_color='grey',
                    background_color='white',
                    header_font=9,
                    enable_click_events=True)

    tab1_layout = [
        [sg.Text('ENVIO AUTOMÁTICO DE MENSAGENS WHATSAPP', size=(50, 0))],
        [sg.Text('-='*45)],
        [sg.Text('Digite a mensagen da 1ª Linha', size=(25, 0)),
         sg.Input(size=(45, 0), key='msg1')],
        [sg.Text('Digite a mensagen da 2ª Linha', size=(25, 0)),
         sg.Input(size=(45, 0), key='msg2')],
        [sg.Text('Digite a mensagen da 3ª Linha', size=(25, 0)),
         sg.Input(size=(45, 0), key='msg3')],
        [sg.Text('-='*45)],
        [sg.Button('Gravar')]
    ]

    tab2_layout = [
        [sg.Text('CADASTROS WHATSAPP', size=(50, 0))],
        [sg.Text('-='*45)],
        [sg.Text('Número', size=(0, 0)), sg.Input(size=(13, 0), key='num'),
         sg.Text('Grupo', size=(0, 0)), sg.Input(size=(2, 0), key='grp')
         ],
        [tbl1],
        [sg.Text('-='*45)],
        [sg.Button('Gravar Numero'), sg.Button('Excluir Numero')]
    ]

    tab3_layout = [
        [sg.Text('ENVIAR MENSAGEM', size=(50, 0))],
        [sg.Text('-='*45)],
        [sg.Button('Enviar WhatsApp com imagem', size=(67, 2))],
        [sg.Button('Enviar WhatsApp sem imagem', size=(67, 2))],
        [sg.Text('-='*45)],
    ]

    layout = [
        [[sg.TabGroup([[sg.Tab('Mensagem', tab1_layout), sg.Tab('Gravar Número', tab2_layout), sg.Tab('Enviar Whatsapp', tab3_layout)]])]
         ]]

    window = sg.Window('MultWhats', layout=layout, finalize=True)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == 'Gravar':

            msg1 = values['msg1']
            msg2 = values['msg2']
            msg3 = values['msg3']
            sg.popup(f'Mensagens gravadas com sucesso!')
            sg.popup(
                f'Para anexar: Vá até a imagem a ser enviada click com o botão direito do mouse e selecione "Copiar Imagem".')

        if event == 'Gravar Numero':

            numero = values['num']
            enviado = 0
            grupo = values['grp']

            gravar = f"INSERT INTO whatsapp (celfone, enviado, grupo) VALUES ({numero}, {enviado}, {grupo})"
            bd.Insert_dados(gravar)
            sg.popup(
                f'O numero de whatsapp {numero} foi cadastrado com sucesso!')

        if event == 'Excluir Numero':

            numero = values['num']
            delete = (f'delete from whatsapp where celfone = {numero};')
            bd.Delet_dados(delete)
            sg.popup(
                f'O numero de whatsapp {numero} foi excluido com sucesso!')

        if event == 'Enviar WhatsApp com imagem':

            msg1 = values['msg1']
            msg2 = values['msg2']
            msg3 = values['msg3']
            WhatsImg(msg1, msg2, msg3)

        if event == 'Enviar WhatsApp sem imagem':

            msg1 = values['msg1']
            msg2 = values['msg2']
            msg3 = values['msg3']
            Whats(msg1, msg2, msg3)


def Chave():

    import ML_Bd_sqlite as bd
    import PySimpleGUI as sg

    select = ('SELECT chave, codex FROM ch_acesso;')
    bd.Consult_dados(select)
    df = bd.Consult_dados(select)

    for fone in df.index:
        chave = df['chave'][fone]
        codex = df['codex'][fone]

    if chave == codex:
        AppWhats()

    else:

        layout = [
            [sg.Text('CHAVE DE ACESSO', size=(0, 0))],
            [sg.Text('-='*20)],
            [sg.Text('Digite a chave de acesso', size=(0, 0)), sg.Input(
                size=(10, 0),  password_char='*', key='chave')],
            [sg.Text('-='*20)],
            [sg.Button('Gravar')]
        ]

        window = sg.Window('Cadastro Motoristas', layout=layout, finalize=True)

        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                break

            if event == 'Gravar':
                chave = int(values['chave'])
                if chave != codex:
                    sg.popup('Chave incorreta!')
                    window.close()
                    Chave()
                else:
                    update = (f'update ch_acesso set chave ={chave};')
                    bd.Update_dados(update)
                    window.close()
                    Chave()


Chave()
