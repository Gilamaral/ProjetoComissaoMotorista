
def LancarCte():

    import mysql.connector

    continuar = 's'
    senhahost = 'dulguiga16'

    while True:

        if continuar != 's':
            break
        
        
        lista = (int(input(f'{"Digite o codigo do motorista:":.<50}')),
                str(input(f'{"Digite a data do CTE:":.<50}')),
                int(input(f'{"Digite o numero do CTE:":.<50}')),
                int(input(f'{"Digite o valor do frete":.<50}')),
                int(input(f'{"Digite o valor do custo com diesel":.<50}')),
                int(input(f'{"Digite o valor do custo com Arla":.<50}')),
                int(input(f'{"Digite o valor do custo com pneu":.<50}')),
                int(input(f'{"Digite o valor do custo com oficina":.<50}')),
                int(input(f'{"Digite o valor do custo com desp. da viagem":.<50}')),
                int(input(f'{"Digite o valor do custo com outras despesas":.<50}'))
                )

        mybd = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd=senhahost,
            database='comissaom'
        )
        mycursor = mybd.cursor()
        if mybd.is_connected():
            print('conectado')

        gravar = "INSERT INTO cte (codmot, datacte, numcte, v_frete, diesel, V_varla, v_pneu, v_oficina, v_desp_viagem, v_outras_desp) VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)"
        mycursor.execute(gravar, lista)
        mybd.commit()
        print(mycursor.rowcount, "record inserted.")

        continuar = input('Deseja continuar lançando cte? [s/n]')
    
    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return


def CadastroM():

    import mysql.connector

    continuar = 's'
    senhahost = 'dulguiga16'

    while True:

        if continuar != 's':
            break
        
        lista  = (
            input(f'{"Digite o nome: ":.<50}'),
            input(f'{"Digite o CPF, somente numeros: ":.<50}'),
            input(f'{"Digite o numero da habilitação: ":.<50}'),
            input(f'{"Digite o nome da rua:":.<50}'),
            int(input(f'{"Digite o numero da residencia: ":.<50}')),
            input(f'{"Digite o bairro: ":.<50}'),
            input(f'{"Digite a cidade: ":.<50}'),
            input(f'{"Digite a UF: ":.<50}'),
                )
        
        #lista = 'Gilvan', '11111111111', '88888888', 'rio solimoes', 816, 'colina verde', 'maringa', 'pr'
        print (lista)
        
        mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=senhahost,
        database='comissaom'
        )
        mycursor = mybd.cursor()
        if mybd.is_connected():
            print('conectado')

        gravar = "insert into cadastromot (nome, cpf, habilitacao, rua, numero, bairro, cidade,uf) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(gravar, lista)
        mybd.commit()
        print(mycursor.rowcount, "record inserted.")

        continuar = input('Deseja continuar lançando cte? [s/n]')
    
    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return
