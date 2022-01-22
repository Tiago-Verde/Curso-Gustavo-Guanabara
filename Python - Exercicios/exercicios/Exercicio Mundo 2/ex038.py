# ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS  MOSTRANDO NA TELA UMA DAS SEGUINTES MENSAGEM. 
# O PRIMEIRO VALOR É MAIOR
# O SEGUNDO VALOR É MAIOR
# NÃO EXISTE VALOR MAIOR, OS NUMEROS SÃO IGUAIS

numero1 = int(input('Informe o primeiro valor: '))
numero2 = int(input('Informe o segundo valor: '))


if numero2 > numero1:
    print('O numero {} é maior que o numero {}'.format(numero2, numero1))
elif numero1 > numero2:
    print('O numero {} é maior que o numero {}'.format(numero1, numero2))
else:
    print('Os numeros são iguais não existe valor maior')
