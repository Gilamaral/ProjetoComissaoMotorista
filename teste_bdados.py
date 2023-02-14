import pandas as pd
import mysql.connector


cadastro = mysql.connector.connect (
    host ='localhost',
    user = 'root',
    passwd = 'dulguiga16',
    database = 'cadastro'
    #table = 'pessoas'
)

conexao = cadastro.cursor()
if cadastro.is_connected():
    print('Banco de dados cadastro está conectado!')

consulta = ('Select * from pessoas')
df = pd.read_sql(consulta, cadastro)
tab_pessoas = pd.DataFrame(df)

print(tab_pessoas)
