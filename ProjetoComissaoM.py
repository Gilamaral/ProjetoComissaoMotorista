import openpyxl as op
import func_uteis as ft
import pandas as pd
import time


lancte = input('Deseja lançar cte manualmente?')

if lancte == 's':
    print('lançando cte...!')
    time.sleep(3)

    '''fim = input('Deseja lançar novo CTE? ')

    while True:
        #grava os dados das viagens executadas
        codmot = int(input('Digite o codigo do motorista'))   
        numcte = int(input('Digite o numero do CTE: '))
        vfrete = int(input('Digite o valor do frete: R$'))
        diesel = int(input('Digite o Valor do combustivel gasto: R$'))
        arla = int(input('Digite o Valor do arla gasto: R$'))
        data = str(input('Digite a data do frete: '))

        tabela = op.load_workbook('C:\ProjetosPython\ProjetoComissaoMotorista\BD_Excel\Comissão Motoristas.xlsx')
        comissao = tabela['comissao']
        comissao.append([numcte, vfrete, diesel, arla, data])
        tabela.save('C:\ProjetosPython\ProjetoComissaoMotorista\BD_Excel\Comissão Motoristas.xlsx')
        print('Lançamento Finalizado!')
        fim = input('Deseja continuar lançando CTE? ')
        if fim == 'n':
        break'''

else:
    print('calculando comissão...')
    time.sleep (3)

tabpd = pd.read_excel('C:\ProjetosPython\ProjetoComissaoMotorista\BD_Excel\Comissão Motoristas.xlsx')
tabpd = tabpd.set_index('numcte')

cst_codmot = int(input('Digite o codigo do motorista: '))

tabpd = tabpd.loc[(tabpd['CodMot'] == cst_codmot)]
print(tabpd)

sum_vfrete = tabpd['vfrete'].sum ()
sum_diesel = tabpd['diesel'].sum ()
sum_arla = tabpd['arla'].sum ()
desp_total = (sum_diesel+ sum_arla)
comissao = sum_vfrete * 0.15

Lista = [sum_vfrete, sum_diesel,sum_arla]
print('-=-'*20)
print('-=-'*20)
print('vfrete R${} - diesel R${} - arla R${}'.format(sum_vfrete,sum_diesel,sum_arla))
print('-=-'*20)
print('# A despesa total do motorista foi: R${:.2f}'.format(desp_total))
print('-=-'*20)
print('# O faturamento total do motorista foi: R${:.2f}'.format(sum_vfrete))
print('-=-'*20)
print('# A comissão total do motorista foi: R${:.2f}'.format(comissao))
print('-=-'*20)
print('-=-'*20)
'''


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def pontos (mm):
    return mm / 0.352777


pdf = canvas.Canvas ('./teste.pdf', pagesize=A4)

txttitulo = 'COMISSÃO MOTORISTA'
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(270), txttitulo)

txttabela = tabpd
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(220), txttabela)

txtdespesas = Lista
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(200), txtdespesas)

txtcomissao = comissao
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(150), txtcomissao)


pdf.save()'''