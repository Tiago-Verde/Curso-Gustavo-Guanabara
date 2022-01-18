# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE NA TELA ESSE MESMO PRODUTO COM DESCONTO DE 5%
preco = float(input('Qual o valor do produto: '))
desconto = preco - (preco *5/100)
print('O valor do produto com desconto de 5 % é de {}'.format(desconto))