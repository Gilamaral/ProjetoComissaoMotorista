def LancarCte():

    import CMbd_interface as cd
    import PySimpleGUI as sg
    import CMtelas_interface as tl

    while True:

        tela_dados = tl.Dados()

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
            
            cd.Insert_dados(gravar, lista)
            window.close()
