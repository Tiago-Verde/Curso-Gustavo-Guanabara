# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM EM SUA CARTEIRA E INFORME QUANTOS DOLARES É POSSIVEL COMPRAR 
valorCarteira = float(input('Informa qual o valor em reais você possui na carteira: '))
valorDolar = float(input('Informe qual a cotação atual do dolar'))
compraDolar = valorCarteira/valorDolar
print('Com o valor que você tem na carteira é possivel comprar {} dolar'.format(compraDolar))