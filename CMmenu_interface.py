def Menu2():
    
    import PySimpleGUI as sg
    import CMlancar_interface as lci
    import CMrelatorio_intertface as rel
    import CMcomissao_interface as co


    layout = [[sg.Menu([['Cadastro',['Dados cte', 'Motoristas']],
                        ['Relatorio',['Viagens', 'Comissão']],
                        ['Dados',['Limpar comissao','Gerar comissao']],
                        ['Venda']], text_color='black', font=9, pad=(10,10))],
              [sg.Text('.', size=(70,25))],
              ]

    window =sg.Window('Gerador de Comissão para Motoristas', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
                window.close()
                break
        
        else:

            if event == 'Dados cte':
                lci.LancarCte()
            
            if event == 'Viagens':
                rel.ViagemMtela()
            
            if event == 'Comissão':
                rel.ComissaoMtela()
            
            if event == 'Limpar comissao':
                co.Limpacom()
            
            if event == 'Gerar comissao':
                co.Geracom()
                
    return

Menu2()