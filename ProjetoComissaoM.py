import openpyxl as op
import func_uteis as ft
import pandas as pd
import time
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

'''
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
lista = (codmot, dtcte, numcte, v_frete, V_varla, v_pneu,v_oficina, v_desp_viagem, v_outras_desp, diesel)

mycursor.execute(gravar, lista)

mybd.commit()

print(mycursor.rowcount, "record inserted.")











'''

# tabela = op.load_workbook('C:\ProjetosPython\ProjetoComissaoMotorista\BD_Excel\Comissão Motoristas.xlsx')
# comissao = tabela['comissao']
# comissao.append([numcte, vfrete, diesel, arla, data])
# tabela.save('C:\ProjetosPython\ProjetoComissaoMotorista\BD_Excel\Comissão Motoristas.xlsx')
# print('Lançamento Finalizado!')
# fim = input('Deseja continuar lançando CTE? ')

# if fim == 'n':
#    break
# else:
#    print('calculando comissão...')
#    time.sleep (3)
#
# Processa calculo de comissão das viagens
tabpd = pd.read_sql_table ('select * from cte', mybd)
df = pd.DataFrame(tabpd)
df = tabpd.set_index('numcte')

print(df)

#
# cst_codmot = int(input('Digite o codigo do motorista: '))
#
# tabpd = tabpd.loc[(tabpd['CodMot'] == cst_codmot)]
# print(tabpd)
#
# sum_vfrete = tabpd['vfrete'].sum ()
# sum_diesel = tabpd['diesel'].sum ()
# sum_arla = tabpd['arla'].sum ()
# desp_total = (sum_diesel+ sum_arla)
# comissao = sum_vfrete * 0.15

# Lista = [sum_vfrete, sum_diesel,sum_arla]
# print('-=-'*20)
# print('-=-'*20)
# print('vfrete R${:.2f} - diesel R${:.2f} - arla R${:.2f}'.format(sum_vfrete,sum_diesel,sum_arla))
# print('-=-'*20)
# print('# A despesa total do motorista foi: R${:.2f}'.format(desp_total))
# print('-=-'*20)
# print('# O faturamento total do motorista foi: R${:.2f}'.format(sum_vfrete))
# print('-=-'*20)
# print('# A comissao total do motorista foi: R${:.2f}'.format(comissao))
# print('-=-'*20)
# print('-=-'*20)

# Grava resultado da comissão em arquivo de texto
# with open('rascunho.txt', 'w') as arquivo:
#    arquivo.write(str('-=-'*16))
#    arquivo.write('\n           COMISSAO DE MOTORISTAS')
#    arquivo.write(str('\n'))
#    arquivo.write(str('-=-'*16))
#    arquivo.write('\n\n\n {}'.format(tabpd))
#    arquivo.write('\n\n vfrete R${} - diesel R${} - arla R${}'.format(sum_vfrete,sum_diesel,sum_arla))
#    arquivo.write('\n\n A despesa total do motorista foi: R${:.2f}'.format(desp_total))
#    arquivo.write('\n\n O faturamento total do motorista foi: R${:.2f}'.format(sum_vfrete))
#    arquivo.write('\n\n A comissão total do motorista foi: R${:.2f}'.format(comissao))'''
