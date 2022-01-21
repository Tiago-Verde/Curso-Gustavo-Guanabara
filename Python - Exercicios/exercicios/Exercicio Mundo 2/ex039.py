# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORMA DE ACORDO COM SUA IDADE 
# SE ELE AINDA VAI SE ALISTAR
# SE JÁ ESTA NA HORA DELE SE ALISTAR
# SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
# O PROGRAMA AINDA DEVERA MOSTRAR QUANTO TEMPO FALTA OU PASSOU DA DATA DE ALISTAMENTO

import datetime

nascimento = int(input('Por favor informe o ano em que você nasceu '))
dataAtual = datetime.date.today().year
alistamento = dataAtual - nascimento
if alistamento < 18:
    print('Você ainda não precisa se alistar você tem {} anos'.format(alistamento))
elif alistamento == 18:
    print('Chegou a hora de seu alistamento você tem {} anos!!!!'.format(alistamento))
else:
    print('O seu alistamento está atrasado você tem {} anos'.format(alistamento))
