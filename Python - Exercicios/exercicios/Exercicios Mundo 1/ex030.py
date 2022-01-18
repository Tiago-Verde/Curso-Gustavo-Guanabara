# CRIE UM PROGRAMA QUE LEIA UM NUMERO INTERIO QUALQUER E FAÇA O PROGRAMA INFORMAR SE O NUMERO É PAR OU IMPAR

numero = int(input('Informe um numero inteiro qualquer: '))
resultado = numero%2
if resultado == 1:
    print('Numero impar')
else:
    print('Numero par')
