import mysql.connector
import pandas as pd

senhahost = 'dulguiga16'

mybd = mysql.connector.connect(
    host='localhost',
    database = 'comissaom',
    user='root',
    passwd= senhahost
)

if mybd.is_connected():
    print('conectado')

cursor = mybd.cursor()

tabbd = ('select * from cte;')
df = pd.read_sql (tabbd,mybd)
print(df)


if mybd.is_connected():
    mybd.close()
    print('desconectado')
