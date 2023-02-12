import openpyxl as op
import func_uteis as ft
import pandas as pd


tabpd = pd.read_excel('C:\ProjetosPython\ProjetoComissaoMotorista\BD_Excel\Comissão Motoristas.xlsx')
tabpd = tabpd.set_index('numcte')

print (tabpd)