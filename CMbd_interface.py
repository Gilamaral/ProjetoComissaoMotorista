
def Insert_dados(gravar, lista):

    import mysql.connector

    mybd = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    passwd='dulguiga16',
                    database='comissaom'
    )

    mycursor = mybd.cursor()

    mycursor.execute(gravar, lista)
    mybd.commit()
    mybd.close()


def Consult_dados(select):

    import mysql.connector
    import pandas as pd

    mybd = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    passwd='dulguiga16',
                    database='comissaom'
    )
    
    tb = (select)
    df = pd.read_sql(tb, mybd)
    tb = pd.DataFrame(df)
    
    mybd.close()
    return(tb)


def Delet_dados(delet):

    import mysql.connector
    
    mybd = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    passwd='dulguiga16',
                    database='comissaom'
    )
    mycursor = mybd.cursor()
    tb = (delet)
    mycursor.execute(tb)
    mybd.commit()
    
    mybd.close()
