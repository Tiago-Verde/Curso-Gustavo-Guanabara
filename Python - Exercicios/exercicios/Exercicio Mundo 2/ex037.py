# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER QUAL A BASE DE CONVERSÃO
# 1 - PARA BINARIO
# 2 - PARA OCTAL
# 3 - PARA HEXADECIMAL

numero = int(input('Informe um numero inteiro qualquer: '))
base = str(input('O numero deve ser convertido para qual base?')).upper()
if base == 'BINARIO':
    binario = bin(numero)
    print('O numero informado na base binária é: {}'.format(binario))
elif base == 'OCTAL':
    octal = oct(numero)
    print('O numero informado na base octal é: {}'.format(octal))
else:
    hexa = hex(numero)
    print('O numero informado na base hexadecimal é: {}'.format(hexa))

