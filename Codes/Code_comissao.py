
def Geracom():
    import pandas as pd
    import mysql.connector

    senhahost = 'dulguiga16'

    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd = senhahost,
        database='comissaom'
    )
    mycursor = mybd.cursor()
    if mybd.is_connected():
        print('conectado')

    
    tabpd = ('select codmot, sum(v_frete) as faturado, sum(V_varla) + sum(diesel) as combustivel, sum(V_desp_viagem) as desp_viag , sum(v_pneu) + sum(v_oficina) + sum(v_outras_desp) as out_desp, (sum(v_frete) - ( sum(V_varla) + sum(diesel) + sum(V_desp_viagem) + sum(v_pneu) + sum(v_oficina) + sum(v_outras_desp))) * 0.15 as comissao from cte group by codmot order by codmot;')
    df = pd.read_sql(tabpd, mybd)
    tabpd1 = pd.DataFrame(df)


    for i in tabpd1.index:
        grav = int(tabpd1['codmot'][i]), int(tabpd1['faturado'][i]), int(tabpd1['combustivel'][i]), int(tabpd1['desp_viag'][i]), int(tabpd1['out_desp'][i]), int(tabpd1['comissao'][i])

        query = "INSERT INTO comissao (codmot, faturado, combustivel, desp_viag, out_desp, comissao) VALUES (%s,%s,%s,%s,%s,%s)"
        gravarlista = (grav)

        mycursor.execute(query, gravarlista)
        mybd.commit()
        print(mycursor.rowcount, "record inserted.")

    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return


def Limpacom():
    import mysql.connector

    senhahost = 'dulguiga16'

    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    mycursor = mybd.cursor()
    if mybd.is_connected():
        print('conectado')

    tabpd = ('delete from comissao;')
    mycursor.execute(tabpd)
    mybd.commit()
    print(mycursor.rowcount, "record inserted.")
    
    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return

