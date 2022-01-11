# CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE A SUA PORÇÃO INTEIRA
# EX: 6.127 - RESULTA 6

import math

numero = float(input('Informe um numero real: '))
convertido = math.trunc(numero)
print('O valor convertido é: {}'.format(convertido))