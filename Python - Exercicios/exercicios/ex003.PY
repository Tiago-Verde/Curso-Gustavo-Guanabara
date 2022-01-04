# CRIE UM PROGRAMA QUE LEIA DOIS NUMEROS E MOSTREA SOMA ENTRE ELES

nome = str(input('Qual o seu nome: ')).upper()
n1 = int(input('Informa um valor para que seja realizado a soma: '))
n2 = int(input('Informe um segundo valor: '))
soma= (n1+n2)
print('{} o resultado de {} + {} é igual a {}'.format(nome, n1, n2, soma))