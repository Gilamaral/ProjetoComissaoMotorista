import pandas as pd
import mysql.connector
import time

mybd = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='dulguiga16',
    database='comissaom'
)
mycursor = mybd.cursor()
if mybd.is_connected():
    print('conectado')

lancar = str(input('deseja lancar manualmente?'))

while True:
    if lancar == 's':
        codmot = int(input('Digite o codigo do motorista: '))
        dtcte = str(input('Digite a data do frete: '))
        numcte = int(input('Digite o numero do CTE: '))
        v_frete = int(input('Digite o valor do frete: R$'))
        diesel = int(input('Digite o valor do combustivel gasto: R$'))
        V_varla = int(input('Digite o valor gasto com arla : R$'))
        v_pneu = int(input('Digite o valor gasto com pneu : R$'))
        v_oficina = int(input('Digite o valor gasto com oficina : R$'))
        v_desp_viagem = int(input('Digite o valor gasto com despesas da viagem : R$'))
        v_outras_desp = int(input('Digite o valor gasto com outras despesas : R$'))

        gravar = "INSERT INTO cte (codmot,datacte,numcte,v_frete,V_varla,v_pneu,v_oficina,v_desp_viagem,v_outras_desp,diesel) VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)"
        lista = (codmot, dtcte, numcte, v_frete, V_varla, v_pneu,
                v_oficina, v_desp_viagem, v_outras_desp, diesel)

        mycursor.execute(gravar, lista)
        mybd.commit()
        print(mycursor.rowcount, "record inserted.")
        lancar = str(input('Deseja continuar lancando cte?'))
    else:
        print('Lançamento finalizado!')
        break