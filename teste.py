import PySimpleGUI as sg
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
df = pd.read_sql('select * from comissao;', mybd)
tab2 = df.set_index('codmot')
sg.popup(tab2, title='teste', font=('', 10,''), line_width=1200)
 
if mybd.is_connected():
    mybd.close()
    print('desconectado')    
