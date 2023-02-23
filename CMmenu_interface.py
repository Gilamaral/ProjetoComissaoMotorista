def Menu2():
    
    import PySimpleGUI as sg
    import CMcomissao_interface as lci


    menu_def =  [
                ['cadastro',['clientes', 'motoristas']],
                ['relatorio'],
                ['venda']
                ]


    layout = [[sg.Menu(menu_def, text_color='black', font="SYSTEM_DEFAULT", pad=(10,10))],
              [sg.Text('.', size=(80,10))] 
            ]

    window =sg.Window('Menu Example', layout)

    while True:
        event,values=window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
                break
        
        else:

            if event == 'motoristas':
                lci.LancarCte()
                Menu2()
    window.close()           
    return

Menu2()