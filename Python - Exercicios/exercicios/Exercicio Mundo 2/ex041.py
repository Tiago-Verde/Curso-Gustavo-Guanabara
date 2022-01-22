# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA POR IDADE
# ATÉ 9 ANOS MIRIM
# ATÉ 14 ANOS INFANTIL
# ATÉ 19 ANOS JUNIOR
# ATÉ 20 SENIOR
# ACIMA MASTER

import datetime

nascimento = int(input('Por favor informe o ano em que você nasceu '))
dataAtual = datetime.date.today().year

categoria = dataAtual - nascimento

if categoria <= 9:
    print('Atleta pertence a categoria mirim com idade de {}'.format(categoria))
elif (categoria > 9) and (categoria <= 14):
    print('Atleta pertence a categoria infantil com idade de {}'.format(categoria))
elif (categoria >14) and (categoria <= 19):
    print('Atleta pertence a categoria junior com idade de {}'.format(categoria))
elif (categoria == 20):
    print('Atleta pertence a categoria senior com idade de {}'.format(categoria))
else:
    print('Atleta pertence a categoria master com idade de {}'.format(categoria))