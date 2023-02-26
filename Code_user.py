def Cpf(cpf):
    numcpf = str(cpf) 
    
    cpf = (len(numcpf))

    if cpf == 11:
        print('Ok, Quantidade de numeros validado!')
    else:
        print('numero errado digite novamente')

    numcpf = str(numcpf)

    cpf1 = numcpf[0]
    cpf2 = numcpf[1]
    cpf3 = numcpf[2]
    cpf4 = numcpf[3]
    cpf5 = numcpf[4]
    cpf6 = numcpf[5]
    cpf7 = numcpf[6]
    cpf8 = numcpf[7]
    cpf9 = numcpf[8]
    cpf10 = numcpf[9]
    cpf11 = numcpf[10]


    cpfg_d1 = (int(cpf1)*10 + int(cpf2)*9 + int(cpf3)*8 + int(cpf4)*7 + int(cpf5)*6 + int(cpf6)*5 + int(cpf7)*4 + int(cpf8)*3 + int(cpf9)*2) % 11
    if cpfg_d1 >= 2:    
        cpfg_d1 = 11 - cpfg_d1
    else:
        cpfg_d1 = 0

    cpfg_d2 = (int(cpf1)*11 + int(cpf2)*10 + int(cpf3)*9 + int(cpf4)*8 + int(cpf5)*7 + int(cpf6)*6 + int(cpf7)*5 + int(cpf8)*4 + int(cpf9)*3 + cpfg_d1*2) %11
    if cpfg_d2 >= 2:    
        cpfg_d2 = 11 - cpfg_d2
    else:
        cpfg_d2 = 0

    valid = cpfg_d1 + cpfg_d2
    digit = int(cpf10) + int(cpf11)

    if digit == valid:
        print('Cpf Valido')
    else:
        print('Cpf Invalido')



cpf = int(input('Digite o numero do cpf sem pontos ou traço: '))
Cpf(cpf)



