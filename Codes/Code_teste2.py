import PySimpleGUI as psg
import CMbd_interface as co

#psg.set_options(font=("Arial Bold", 14))
df = []
select = ('select * from comissao;')
co.Consult_dados(select)
df = co.Consult_dados(select)

tabpd1 = df
#grav1 = []
d = 30

for i in tabpd1.index:
    grav1 = [[tabpd1['codmot'][i], tabpd1['faturado'][i], tabpd1['combustivel'][i], tabpd1['desp_viag'][i], tabpd1['out_desp'][i], tabpd1['comissao'][i]],]

    print(grav1)