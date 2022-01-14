# FAÇA UM PROGRAMA QUE LEIA TRES NUMEROS INTEIROS E APRESENTA QUAL O MAIOR E O MENOR NUMERO
n1 = int(input('Informe o primeiro valor:'))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))

maior = n1

if n2 > n1:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior valor é {}'.format(maior))

menor = n1

if n2 < n1:
    menor = n2
if n3 < menor:
    menor = n3
print('O menor valor é {}'.format(menor))
    


