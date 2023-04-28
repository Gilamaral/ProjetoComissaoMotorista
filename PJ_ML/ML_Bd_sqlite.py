def Consult_dados(select):

    import sqlite3
    import pandas as pd

    conex = sqlite3.connect('C:/SqLite/appml.db')

    tb = (select)
    df = pd.read_sql(tb, conex)
    tb = pd.DataFrame(df)

    return(tb)


def Update_dados(update):

    import sqlite3

    conex = sqlite3.connect('C:/SqLite/appml.db')

    mycursor = conex.cursor()
    mycursor.execute(update)
    conex.commit()
    conex.close()


def Insert_dados(gravar):

    import sqlite3

    conex = sqlite3.connect('C:/SqLite/appml.db')

    mycursor = conex.cursor()

    mycursor.execute(gravar)
    conex.commit()
    conex.close()


def Delet_dados(delet):

    import sqlite3

    conex = sqlite3.connect('C:/SqLite/appml.db')

    mycursor = conex.cursor()
    tb = (delet)
    mycursor.execute(tb)
    conex.commit()
    conex.close()