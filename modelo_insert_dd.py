def Modeloinsertdd():

    import mysql.connector

    continuar = 's'
    senhahost = 'dulguiga16'

    while True:

        if continuar != 's':
            break

        lista  = (input(f'{"":.<50}'),
                    int(input(f'{"":.<50}')),
                    
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

        gravar = "INSERT INTO cte ('') VALUES (%s,)"
        mycursor.execute(gravar, lista)
        mybd.commit()
        print(mycursor.rowcount, "record inserted.")

        continuar = input('Deseja continuar lançando cte? [s/n]')
    
    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return
