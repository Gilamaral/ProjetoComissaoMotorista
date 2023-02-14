import pandas as pd
import mysql.connector

mybd = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='dulguiga16',
    database='comissaom'
)

mycursor = mybd.cursor()

if mybd.is_connected():
    print('conectado')

# Processa calculo de comissão das viagens
tabpd = ('select * from cte;')
df = pd.read_sql(tabpd, mybd)
tabcomissao = pd.DataFrame(df)
# df = tabpd.set_index('numcte')

#print(tabcomissao)

lancar = 's'

while True:
    
    if lancar == 's':
        #
        cst_codmot = int(input('Digite o codigo do motorista: '))
        tabpd = tabcomissao.loc[tabcomissao['codmot']== cst_codmot ]
        #print(tabpd)
        #
        faturado = tabpd['v_frete'].sum ()
        desp_viag = tabpd['V_desp_viagem'].sum ()
        out_desp = tabpd['V_varla'].sum ()
        diesel = tabpd['diesel'].sum ()
        arla = tabpd['V_varla'].sum ()
        combustivel = float(diesel + arla)
        comissao = faturado * 0.15


        gravar = "INSERT INTO comissao (codmot, faturado, combustivel,  desp_viag, out_desp, comissao) VALUES (%s,%s,%s,%s,%s,%s)"
        lista = (cst_codmot, faturado, combustivel, desp_viag, out_desp, comissao)

        mycursor.execute(gravar, lista)
        mybd.commit()
        print(mycursor.rowcount, "record inserted.")
        lancar = str(input('Gerar comissão de outro motorista [s/n]? '))        
    else:
        print('Lançamento finalizado!')
        break
