# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E INFORME SE É UM ANO BISSEXTO OU NÃO

ano = int(input('Informe o ano:'))
if (ano % 4 ==0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print('Ano bissexto')
else:
    print('Não é bissexto')        



