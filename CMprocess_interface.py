
def Geracom():
    import PySimpleGUI as sg
    import CMbd_interface as co

    select = ('select codmot, sum(v_frete) as faturado, sum(V_varla) + sum(diesel) as combustivel, sum(V_desp_viagem) as desp_viag , sum(v_pneu) + sum(v_oficina) + sum(v_outras_desp) as out_desp, (sum(v_frete) - ( sum(V_varla) + sum(diesel) + sum(V_desp_viagem) + sum(v_pneu) + sum(v_oficina) + sum(v_outras_desp))) * 0.15 as comissao from cte group by codmot order by codmot;')
    co.Consult_dados(select)
    tabpd1 = co.Consult_dados(select)
    sg.popup('Consulta Executada!')

    for i in tabpd1.index:
        grav = int(tabpd1['codmot'][i]), int(tabpd1['faturado'][i]), int(tabpd1['combustivel'][i]), int(tabpd1['desp_viag'][i]), int(tabpd1['out_desp'][i]), int(tabpd1['comissao'][i])

        gravar = "INSERT INTO comissao (codmot, faturado, combustivel, desp_viag, out_desp, comissao) VALUES (%s,%s,%s,%s,%s,%s)"
        lista = (grav)

        co.Insert_dados(gravar, lista)
    sg.popup('record inserted.')



def Limpacom():

    import PySimpleGUI as sg
    import CMbd_interface as co

    delet = ('delete from comissao;')
    co.Delet_dados(delet)
    
    sg.popup('Tabela Comissão liberada!')
