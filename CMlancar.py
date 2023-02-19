
def LancarCte():
    import mysql.connector

    continuar = 's'
    senhahost = input('Digite a senha de acesso ao banco de dados: ')

    while True:

        if continuar == 'n':
            break

        lista = (int(input('Digite o codigo do motorista: ')),
                str(input('Digite a data do CTE: ')),
                int(input('Digite o numero do CTE: ')),
                int(input('Digite o valor do frete R$ ')),
                int(input('Digite o valor do custo com diesel R$ ')),
                int(input('Digite o valor do custo com Arla R$ ')),
                int(input('Digite o valor do custo com pneu R$ ')),
                int(input('Digite o valor do custo com oficina R$ ')),
                int(input('Digite o valor do custo com desp. da viagem R$ ')),
                int(input('Digite o valor do custo com outras despesas R$ '))
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
        gravarlista = (lista)

        mycursor.execute(gravar, lista)
        mybd.commit()
        print(mycursor.rowcount, "record inserted.")

        continuar = input('Deseja continuar lançando cte? [s/n]')
    return

