
def Insert_dados(gravar, lista):

    import mysql.connector

    mybd = mysql.connector.connect(
                    host='web128.f1.k8.com.br',
                    user='apptruckar',
                    passwd='',
                    database='apptruckar'
    )

    if mybd.is_connected():
        print('conectado')


    mycursor = mybd.cursor()

    mycursor.execute(gravar, lista)
    mybd.commit()
    mybd.close()


def Consult_dados(select):

    import mysql.connector
    import pandas as pd

    mybd = mysql.connector.connect(
                    host='web128.f1.k8.com.br',
                    user='apptruckar',
                    passwd='',
                    database='apptruckar'
    )
    
    tb = (select)
    df = pd.read_sql(tb, mybd)
    tb = pd.DataFrame(df)
    
    mybd.close()
    return(tb)


def Delet_dados(delet):

    import mysql.connector
    
    mybd = mysql.connector.connect(
                    host='web128.f1.k8.com.br',
                    user='apptruckar',
                    passwd='',
                    database='apptruckar'
    )
    mycursor = mybd.cursor()
    tb = (delet)
    mycursor.execute(tb)
    mybd.commit()
    
    mybd.close()


