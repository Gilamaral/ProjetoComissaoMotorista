
def Menu():
    import CMlancar as lc
    import CMcomissao as cm
    import CMrelatorio as rt
    import os

    os.system('cls')
    print('-'*55)
    print(f'{"SISTEMA CALCULO DE COMISSAO":^55}')
    print('-'*55)
    print('  0 - Sair')
    print('  1 - Lançar Cte')
    print('  2 - Gerar comissão')
    print('  3 - Limpa comissão')
    print('  4 - Cadastro de Motoristas')
    print('-'*55)
    print(f'{"Relatorios":^55}')
    print('-'*55)
    print('  11 - Rel. Viagem realizadas')
    print('  12 - Rel. Comissão do periodo')
    print('-'*55)

    programa = int(input('Digite a opção acima: '))

    if programa == 0:
        print('Até logo!')
    else:

        if programa == 1:
            lc.LancarCte()
            os.system('cls')
            Menu()

        if programa == 2:
            cm.Geracom()
            os.system('cls')
            Menu()

        if programa == 4:
            lc.CadastroM()
            os.system('cls')
            Menu()
        
        
        if programa == 11:
            rt.ViagemM()
            os.system('cls')
            Menu()

        if programa == 12:
            rt.ComissaoM()
            os.system('cls')
            Menu()
    return

Menu()
