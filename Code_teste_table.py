import PySimpleGUI as psg
import CMbd_interface as co

psg.set_options(font=("Arial Bold", 9))
df = []
select = ('select * from comissao;')
co.Consult_dados(select)
df = co.Consult_dados(select)

print(df)

tabpd1 = df
grav1 = []

for i in tabpd1.index:
    grav = [tabpd1['codmot'][i], tabpd1['faturado'][i], tabpd1['combustivel'][i], tabpd1['desp_viag'][i], tabpd1['out_desp'][i], tabpd1['comissao'][i]]
    grav1.append(grav)


titulo = ['codmot', 'faturado', 'combustivel', 'desp_viag', 'out_desp', 'comissao']

tbl1 = psg.Table(values=grav1,
                headings=titulo,
                auto_size_columns=True,
                display_row_numbers=False,
                text_color='black',
                justification='center',
                key='-TABLE-',
                selected_row_colors='red on yellow',
                enable_events=True,
                expand_x=False,
                expand_y=False,
                alternating_row_color= 'grey',
                background_color='white' ,
                header_font=12,
                enable_click_events=True)

layout = [[tbl1]]

window = psg.Window("Comissão por motorista", layout, size=(600, 200), resizable=True)

while True:
   event, values = window.read()
   #print("event:", event, "values:", values)

   if event == psg.WIN_CLOSED:
      break
  
window.close()
