def ViagemM():
    import pandas as pd
    import mysql.connector

    senhahost = 'dulguiga16'
   
    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    mybd.cursor()
    
    cst_codmot = int(input('Digite o motorista: '))

    tabpd = ('select * from cte;')
    df = pd.read_sql(tabpd, mybd)
    df = df.loc[df['codmot'] == cst_codmot]
    print(df)

    sair = input('Digite Enter para fechar')
    print('Fim do relatorio!')

    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return


def ComissaoM():
    import pandas as pd
    import mysql.connector

    senhahost = 'dulguiga16'

    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd= senhahost,
        database='comissaom'
    )
    mybd.cursor()
   
    tabpd = ('select * from comissao;')
    df = pd.read_sql(tabpd, mybd)
    print(df)

    sair = input('Digite Enter para fechar')
    print('Fim do relatorio!')

    if mybd.is_connected():
        mybd.close()
        print('desconectado')
    return
