def Menu2():
    
    import PySimpleGUI as sg
    import CMcadastros_interface as lci
    import CMrelatorio_intertface as rel
    import CMprocess_interface as co


    layout = [[sg.Menu([['Cadastros',['Lançar cte', 'Motoristas', 'Veiculos', 'Pneus', 'Combustivel','Peças']],
                        ['Relatorios',['Viagens', 'Comissão', 'Veículo', 'Pneus', 'Peças']],
                        ['Processamento de Dados',['Limpar Comissao','Gerar Comissao']],
                        ['Consultas',['Pneus','Peças','Combustive','veículo']]], text_color='black', font=9, pad=(10,10))],
              [sg.Text('.', size=(70,25))],
              ]

    window =sg.Window('Gerador de Comissão para Motoristas', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
                window.close()
                break
        
        else:

            if event == 'Lançar cte':
                lci.LancarCte()
            
            if event == 'Viagens':
                rel.ViagemMtela()
            
            if event == 'Comissão':
                rel.ComissaoMtela()
            
            if event == 'Limpar Comissao':
                co.Limpacom()
            
            if event == 'Gerar Comissao':
                co.Geracom()
                
    return



Menu2()