'''Arquivo =  open('rascunho.txt', 'w')
Arquivo.write ('ola mundo')
Arquivo.close()'''


with open('rascunho.txt', 'w') as arquivo:
    texto = 'como vai, tudo bem'
    arquivo.write (texto)



'''with open ('rascunho.txt', 'r', encoding='jtf-8') as arquivo:
    relatorio = arquivo.read()
print(relatorio)'''
