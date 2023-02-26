
def Cpf():
    import PySimpleGUI as sg

    while True:

        TelaCpf()

        window, event, values = sg.read_all_windows()
        cpf = values['cpf']

        #verificando numeros informados
        #------------------------------------------#
        numcpf = str(cpf) 
        cpf = (len(numcpf))

        if cpf != 11:
            sg.popup('numero errado digite novamente', title='resultado')
            break
        else:
            sg.popup('Ok, Quantidade de numeros validado!', title='resultado')

            #calculando o primeiro digito
            #------------------------------------------#
            d1 = 10
            calc1 = []
            for i in numcpf[:9]:
                calc1 += int(i) * d1,
                d1 -= 1
            calc1 = sum(calc1)
            calc1 = calc1 % 11
            
            if calc1 >= 2:    
                dig1 = 11 - calc1
            else:
                dig1 = 0    
            
            #calculando o segundo digito
            #------------------------------------------#
            d2 = 11
            calc2 = []
            for i in numcpf[:9]:
                calc2 += int(i) * d2,
                d2 -= 1
            calc2 = sum(calc2) + (dig1 *2)
            calc2 = calc2 % 11
        
            if calc2 >= 2:    
                dig2 = 11 - calc2
            else:
                dig2 = 0    

            valid = [dig1, dig2]
            
            #Validando CPF
            #------------------------------------------#
            digito = []
            for i in numcpf[9:]:
                digito += int(i),
            

            if digito == valid:
                sg.popup('Cpf Valido', title='resultado')
            else:
                sg.popup('Cpf Invalido', title='resultado')
        window.close()
        break


def TelaCpf():

    import PySimpleGUI as sg

    layout = [
        [sg.Text('Digite o numero do seu cpf: (somente numeros)', size=(30, 0))], 
        [sg.Input(size=(30, 0), key='cpf')],
        [sg.Button('Enviar dados')]
    ]
    return sg.Window('Validar cpf', layout=layout, finalize=True, size=(250, 120))
